export class Track {
    id: number;
    title: string;
    path: string;
    album: string;
    artist: string;

    constructor(id: number, title: string, path: string, album: string, artist: string) {
        this.id = id;
        this.title = title;
        this.path = path;
        this.album = album;
        this.artist = artist;
    };
}