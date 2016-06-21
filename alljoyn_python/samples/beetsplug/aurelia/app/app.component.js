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
var http_1 = require('@angular/http');
var speakers_component_1 = require('./speakers/speakers.component');
var tracks_component_1 = require('./tracks/tracks.component');
var track_edit_component_1 = require('./track-edit/track-edit.component');
var allplay_service_1 = require('./allplay.service');
var common_1 = require('@angular/common');
var AppComponent = (function () {
    function AppComponent() {
        this.title = 'AllPlay Speaker Control';
        this.isSidebarOff = true;
    }
    AppComponent.prototype.showSpeakers = function (newState) {
        this.isSidebarOff = newState;
    };
    AppComponent = __decorate([
        core_1.Component({
            selector: 'allplay',
            templateUrl: 'app/app.component.html',
            styleUrls: ['app/allplay.css', 'app/simple-sidebar.css'],
            directives: [router_deprecated_1.ROUTER_DIRECTIVES, speakers_component_1.AllPlaySpeakerComponent, common_1.NgClass],
            providers: [allplay_service_1.AllPlayService, http_1.HTTP_PROVIDERS, router_deprecated_1.ROUTER_PROVIDERS],
        }),
        router_deprecated_1.RouteConfig([
            {
                path: '/tracks',
                name: 'Tracks',
                component: tracks_component_1.TrackViewComponent
            },
            {
                path: '/trackedit/:id',
                name: 'TrackEdit',
                component: track_edit_component_1.TrackEditComponent
            },
        ]), 
        __metadata('design:paramtypes', [])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map