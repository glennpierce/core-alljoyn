import {Pipe, PipeTransform} from '@angular/core';
import { Track } from '../track';

@Pipe({
    name: 'trackFilter',
})
export class TrackFilterPipe implements PipeTransform {
    transform(value: any, title: string): any {
       let filter = title.toLocaleLowerCase();
       return filter ? value.filter(track => track.title.toLocaleLowerCase().indexOf(filter) != -1) : value;
    }
}