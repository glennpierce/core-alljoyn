import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router-deprecated';
import { AllPlayService } from '../allplay.service';
import { Track } from '../track';
import { TrackEditComponent } from '../track-edit/track-edit.component';
import { TrackFilterPipe } from '../track-filter/trackFilter';
import { PaginatePipe, PaginationControlsCmp, PaginationService } from 'ng2-pagination';


@Component({
  selector: 'all_tracks',
  templateUrl: 'app/tracks/tracks.component.html',
  directives: [PaginationControlsCmp, TrackEditComponent],
  pipes: [PaginatePipe, TrackFilterPipe],
  providers: [PaginationService]
})
export class TrackViewComponent implements OnInit {
  tracks: Array<Track>;
  private queue: Array<Track>;
  selectedTrack: Track;

  constructor(private router: Router, private allplayService: AllPlayService) {
    this.queue = new Array(100);
  }

  ngOnInit() {
      this.allplayService.getTracks().subscribe(res => this.tracks = res);
  }

  onSelect(track: Track) { this.selectedTrack = track; }

  addToQueue(event: any, track: Track) {
    this.queue.push(track)
    console.log(track);
    event.preventDefault();
  }
  
  gotoTrackEdit(event: any, track: Track) {
    this.router.navigate(['TrackEdit', { id: track.id }]);
    event.preventDefault();
  }
}

