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
var router_deprecated_2 = require('@angular/router-deprecated');
var track_1 = require('../track');
var allplay_service_1 = require('../allplay.service');
var TrackEditComponent = (function () {
    function TrackEditComponent(allplayService, router, routeParams) {
        this.allplayService = allplayService;
        this.router = router;
        this.routeParams = routeParams;
    }
    TrackEditComponent.prototype.ngOnInit = function () {
        var _this = this;
        if (this.routeParams.get('id') !== null) {
            var id = +this.routeParams.get('id');
            //this.navigated = true;
            this.allplayService.getTrack(id)
                .then(function (track) { return _this.track = track; });
        } //else {
        //this.navigated = false;
        //this.hero = new Hero();
        //}
    };
    TrackEditComponent.prototype.cancelMetadata = function () {
        this.router.navigate(['Tracks']);
    };
    TrackEditComponent.prototype.applyMetadata = function () {
        this.allplayService.updateTrackMetadata(this.track);
        this.router.navigate(['Tracks']);
    };
    TrackEditComponent.prototype.goBack = function () {
        window.history.back();
    };
    __decorate([
        core_1.Input(), 
        __metadata('design:type', track_1.Track)
    ], TrackEditComponent.prototype, "track", void 0);
    TrackEditComponent = __decorate([
        core_1.Component({
            selector: 'track-edit',
            templateUrl: 'app/track-edit/track-edit-component.html',
        }), 
        __metadata('design:paramtypes', [allplay_service_1.AllPlayService, router_deprecated_1.Router, router_deprecated_2.RouteParams])
    ], TrackEditComponent);
    return TrackEditComponent;
}());
exports.TrackEditComponent = TrackEditComponent;
//# sourceMappingURL=track-edit.component.js.map