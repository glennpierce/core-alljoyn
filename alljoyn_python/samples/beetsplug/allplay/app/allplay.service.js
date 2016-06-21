"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var http_1 = require('@angular/http');
var Observable_1 = require('rxjs/Observable');
require('rxjs/add/observable/of');
require('rxjs/add/operator/map');
require('rxjs/add/operator/do');
require('rxjs/add/operator/share');
require('rxjs/add/operator/toPromise');
var speaker_1 = require('./speaker');
var AllPlayService = (function () {
    function AllPlayService(http) {
        this.http = http;
        this.baseUrl = 'http://0.0.0.0:8337/'; // URL to web api
        this.updateUrl = 'http://0.0.0.0:8337/update'; // URL to web api
        // http.get('http://127.0.0.1:8337/tracks').map((res:Response) => res.json())
        //           .subscribe(
        //             data => { this.tracks = data},
        //             err => console.error(err),
        //             () => console.log('done')
        //           );
    }
    AllPlayService.prototype.getSpeakers = function () {
        var headers = new http_1.Headers({ 'Content-Type': 'application/json' });
        return this.http.get(this.baseUrl + "get_devices")
            .map(function (responseData) {
            return responseData.json()['devices'];
        })
            .map(function (speakers) {
            var result = [];
            if (speakers) {
                speakers.forEach(function (speaker) {
                    result.push(new speaker_1.Speaker(speaker.id, speaker.state, speaker.name, speaker.volume));
                });
            }
            return result;
        });
    };
    AllPlayService.prototype.setVolume = function (speaker, volume) {
        var headers = new http_1.Headers({ 'Content-Type': 'application/json' });
        return this.http.post('/adjust_volume', JSON.stringify(speaker), { headers: headers })
            .toPromise()
            .then(function (response) { return response.json().data; })
            .catch(this.handleError);
    };
    AllPlayService.prototype.getTracks = function () {
        var _this = this;
        if (this.tracks) {
            return Observable_1.Observable.of(this.tracks);
        }
        // return an observable
        return this.http.get(this.baseUrl + "tracks/")
            .map(function (responseData) {
            return responseData.json()['items'];
        })
            .do(function (tracks) { _this.tracks = tracks; });
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
    };
    AllPlayService.prototype.getTrack = function (id) {
        return this.getTracks().toPromise()
            .then(function (tracks) { return tracks.filter(function (track) { return track.id === id; })[0]; })
            .catch(this.handleError);
    };
    AllPlayService.prototype.updateTrackMetadata = function (track) {
        var headers = new http_1.Headers();
        headers.append('Content-Type', 'application/json');
        var url = '${this.heroesUrl}/${track.id}';
        return this.http
            .put(this.updateUrl, JSON.stringify(track), { headers: headers })
            .toPromise()
            .then(function () { return track; })
            .catch(this.handleError);
    };
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
    AllPlayService.prototype.handleError = function (error) {
        console.error('An error occurred', error);
        return Promise.reject(error.message || error);
    };
    AllPlayService = __decorate([
        core_1.Injectable(), 
        __metadata('design:paramtypes', [http_1.Http])
    ], AllPlayService);
    return AllPlayService;
}());
exports.AllPlayService = AllPlayService;
//# sourceMappingURL=allplay.service.js.map