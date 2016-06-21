"use strict";
var Speaker = (function () {
    function Speaker(id, state, name, volume) {
        this.id = id;
        this.state = state;
        this.name = name;
        this.volume = volume;
    }
    ;
    Object.defineProperty(Speaker.prototype, "selected", {
        get: function () {
            return this._selected;
        },
        set: function (value) {
            this._selected = value;
            alert('hhhssssssssssssssssssssssh');
        },
        enumerable: true,
        configurable: true
    });
    return Speaker;
}());
exports.Speaker = Speaker;
//# sourceMappingURL=speaker.js.map