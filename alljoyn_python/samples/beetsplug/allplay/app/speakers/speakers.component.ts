import { Component } from '@angular/core';
import { AllPlayService } from '../allplay.service';
import { Speaker } from '../speaker';
import {Slider} from 'primeng/primeng';

@Component({
  selector: 'allplay-speakers',
  templateUrl: 'app/speakers/speakers.component.html',
  styleUrls: ['app/speakers/speakers.component.css'],
  directives: [Slider],
})

export class AllPlaySpeakerComponent {
  title = 'Allplay Speakers';
  _speakers: Array<Speaker>;

  constructor(private allplayService: AllPlayService) {
  }

  ngOnInit() {
      this.allplayService.getSpeakers()
        .subscribe(res => this._speakers = res );
  }

  get speakers() : Array<Speaker> {
    return this._speakers;
  } 

  selectedcheckbox(event: any, speaker: Speaker) {
        //recipient.selected = (recipient.selected) ? false : true;
        event.preventDefault();
  }

}
