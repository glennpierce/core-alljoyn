import { Injectable }    from '@angular/core';
import { Http, Headers, Response } from '@angular/http';

import {Observable} from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/share';
import 'rxjs/add/operator/toPromise';

import { Speaker } from './speaker';
import { Track } from './track';

@Injectable()
export class AllPlayService {

  private baseUrl = 'http://0.0.0.0:8337/';  // URL to web api
  private updateUrl = 'http://0.0.0.0:8337/update';  // URL to web api
  //private speakers: Speaker[]; 
  private tracks: Track[];

  constructor(private http: Http)
  { 
      // http.get('http://127.0.0.1:8337/tracks').map((res:Response) => res.json())
      //           .subscribe(
      //             data => { this.tracks = data},
      //             err => console.error(err),
      //             () => console.log('done')
      //           );
  }

  getSpeakers(): Observable<Speaker[]> {

    let headers = new Headers({'Content-Type': 'application/json'});

    return this.http.get(this.baseUrl + "get_devices")
          .map((responseData) => {
              return responseData.json()['devices'];
          })
          // next transform - each element in the 
          // array to a Task class instance
          .map((speakers: Array<any>) => {
            let result : Array<Speaker> = [];
            if (speakers) {
              speakers.forEach((speaker) => {
                result.push(new Speaker(speaker.id, speaker.state, 
                                        speaker.name, speaker.volume));
              });
            }
            return result;  
         });
  }

  setVolume(speaker: Speaker, volume: number) {

    let headers = new Headers({'Content-Type': 'application/json'});

    return this.http.post('/adjust_volume', JSON.stringify(speaker), {headers: headers})
               .toPromise()
               .then(response => response.json().data)
               .catch(this.handleError);
  }

  getTracks() : Observable<Track[]> {
      if (this.tracks) {
        return Observable.of(this.tracks);
      }
    
      // return an observable
      return this.http.get(this.baseUrl + "tracks/")
          .map((responseData) => {
              return responseData.json()['items'];
          })
          .do((tracks) => { this.tracks = tracks });
        
        //  .map((tracks: Array<any>) => {
        //      let result: Array<Track> = [];
        //      if (tracks) {
        //          tracks.forEach((track) => {
        //              result.push(
        //                  new Track(track.id, track.title, track.path, track.album, track.artist));
        //          });
        //      }
        //      return result;
        //  });
  }
  
  getTrack(id: number) {
  
    return this.getTracks().toPromise()             
               .then(tracks => tracks.filter(track => track.id === id)[0])
               .catch(this.handleError);
  }

  updateTrackMetadata(track: Track) {
      let headers = new Headers();
      headers.append('Content-Type', 'application/json');

      let url = '${this.heroesUrl}/${track.id}';

      return this.http
                   .put(this.updateUrl, JSON.stringify(track), {headers: headers})
                   .toPromise()
                   .then(() => track)
                   .catch(this.handleError);
  }
  
  
  /*
  this.updateMetaData = function($http) {
        var parameters = {'item': this.item};
        var json_data = JSON.stringify(parameters);
        return $http({cache: false, url: '/update', method: 'post', data: json_data});
     };
  */
  
/*
  // Add new Hero
  private post(hero: Hero): Promise<Hero> {
    let headers = new Headers({
      'Content-Type': 'application/json'});

    return this.http
               .post(this.heroesUrl, JSON.stringify(hero), {headers: headers})
               .toPromise()
               .then(res => res.json().data)
               .catch(this.handleError);
  }

  // Update existing Hero
  private put(hero: Hero) {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');

    let url = `${this.heroesUrl}/${hero.id}`;

    return this.http
               .put(url, JSON.stringify(hero), {headers: headers})
               .toPromise()
               .then(() => hero)
               .catch(this.handleError);
  }
*/

  private handleError(error: any) {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
}