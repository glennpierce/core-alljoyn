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
var allplay_service_1 = require('../allplay.service');
var primeng_1 = require('primeng/primeng');
var AllPlaySpeakerComponent = (function () {
    function AllPlaySpeakerComponent(allplayService) {
        this.allplayService = allplayService;
        this.title = 'Allplay Speakers';
    }
    AllPlaySpeakerComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.allplayService.getSpeakers()
            .subscribe(function (res) { return _this._speakers = res; });
    };
    Object.defineProperty(AllPlaySpeakerComponent.prototype, "speakers", {
        get: function () {
            return this._speakers;
        },
        enumerable: true,
        configurable: true
    });
    AllPlaySpeakerComponent.prototype.selectedcheckbox = function (event, speaker) {
        //recipient.selected = (recipient.selected) ? false : true;
        event.preventDefault();
    };
    AllPlaySpeakerComponent = __decorate([
        core_1.Component({
            selector: 'allplay-speakers',
            templateUrl: 'app/speakers/speakers.component.html',
            styleUrls: ['app/speakers/speakers.component.css'],
            directives: [primeng_1.Slider],
        }), 
        __metadata('design:paramtypes', [allplay_service_1.AllPlayService])
    ], AllPlaySpeakerComponent);
    return AllPlaySpeakerComponent;
}());
exports.AllPlaySpeakerComponent = AllPlaySpeakerComponent;
//# sourceMappingURL=speakers.component.js.map