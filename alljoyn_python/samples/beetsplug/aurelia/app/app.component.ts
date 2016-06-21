import { Component } from '@angular/core';
import { RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from '@angular/router-deprecated';
import { HTTP_PROVIDERS } from '@angular/http';
import { AllPlaySpeakerComponent } from './speakers/speakers.component';
import { TrackViewComponent } from './tracks/tracks.component';
import { TrackEditComponent } from './track-edit/track-edit.component';
import { AllPlayService } from './allplay.service';
import {NgClass} from '@angular/common';


@Component({
  selector: 'allplay',
  templateUrl: 'app/app.component.html',
  styleUrls: ['app/allplay.css', 'app/simple-sidebar.css'],
  directives: [ROUTER_DIRECTIVES, AllPlaySpeakerComponent, NgClass],
  providers: [AllPlayService, HTTP_PROVIDERS, ROUTER_PROVIDERS],
})
@RouteConfig([
  {
    path: '/tracks',
    name: 'Tracks',
    component: TrackViewComponent
  },
  {
    path: '/trackedit/:id',
    name: 'TrackEdit',
    component: TrackEditComponent
  },
])
export class AppComponent {
  title = 'AllPlay Speaker Control';
  isSidebarOff = true;

  showSpeakers(newState) {
      this.isSidebarOff = newState;
  }
}
