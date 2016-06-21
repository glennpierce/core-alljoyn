import { Component, OnInit, Input } from '@angular/core';
import { Router } from '@angular/router-deprecated';
import { RouteParams } from '@angular/router-deprecated';

import { Track } from '../track';
import { AllPlayService } from '../allplay.service';

@Component({
  selector: 'track-edit',
  templateUrl: 'app/track-edit/track-edit-component.html',
  //styleUrls: ['app/track-edit.component.css']
})
export class TrackEditComponent implements OnInit {
  @Input() track: Track;
  
  constructor(
    private allplayService: AllPlayService,
    private router: Router,
    private routeParams: RouteParams) {
  }

  ngOnInit() {
  
    if (this.routeParams.get('id') !== null) {
      let id = +this.routeParams.get('id');
      //this.navigated = true;
      this.allplayService.getTrack(id)
          .then(track => this.track = track);
    } //else {
      //this.navigated = false;
      //this.hero = new Hero();
    //}
  }
  
  cancelMetadata() {
      this.router.navigate(['Tracks']);
  }

  applyMetadata() {
      this.allplayService.updateTrackMetadata(this.track);
      this.router.navigate(['Tracks']);
  }
  
  goBack() {
    window.history.back();
  }
}