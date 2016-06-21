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
var router_deprecated_1 = require('@angular/router-deprecated');
var allplay_service_1 = require('../allplay.service');
var track_edit_component_1 = require('../track-edit/track-edit.component');
var trackFilter_1 = require('../track-filter/trackFilter');
var ng2_pagination_1 = require('ng2-pagination');
var TrackViewComponent = (function () {
    function TrackViewComponent(router, allplayService) {
        this.router = router;
        this.allplayService = allplayService;
        this.queue = new Array(100);
    }
    TrackViewComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.allplayService.getTracks().subscribe(function (res) { return _this.tracks = res; });
    };
    TrackViewComponent.prototype.onSelect = function (track) { this.selectedTrack = track; };
    TrackViewComponent.prototype.addToQueue = function (event, track) {
        this.queue.push(track);
        console.log(track);
        event.preventDefault();
    };
    TrackViewComponent.prototype.gotoTrackEdit = function (event, track) {
        this.router.navigate(['TrackEdit', { id: track.id }]);
        event.preventDefault();
    };
    TrackViewComponent = __decorate([
        core_1.Component({
            selector: 'all_tracks',
            templateUrl: 'app/tracks/tracks.component.html',
            directives: [ng2_pagination_1.PaginationControlsCmp, track_edit_component_1.TrackEditComponent],
            pipes: [ng2_pagination_1.PaginatePipe, trackFilter_1.TrackFilterPipe],
            providers: [ng2_pagination_1.PaginationService]
        }), 
        __metadata('design:paramtypes', [router_deprecated_1.Router, allplay_service_1.AllPlayService])
    ], TrackViewComponent);
    return TrackViewComponent;
}());
exports.TrackViewComponent = TrackViewComponent;
//# sourceMappingURL=tracks.component.js.map