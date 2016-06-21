export class Speaker {
 
  private _selected: boolean;
  id: string;
  state: string;
  name: string;
  volume: number;

  constructor(id: string, state: string, name: string, volume: number) {
    this.id = id;
    this.state = state;
    this.name = name;
    this.volume = volume;
  };

  get selected(): boolean {
    return this._selected;
  }
 
  set selected(value: boolean) {
    this._selected = value;
    alert('hhhssssssssssssssssssssssh');
  }

  
}