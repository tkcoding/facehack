import { Component, OnInit, Renderer2, ElementRef} from '@angular/core';

@Component({
  selector: 'app-top-nav',
  templateUrl: './top-nav.component.html',
  styleUrls: ['./top-nav.component.css']
})
export class TopNavComponent implements OnInit{
  navCollapsed: boolean;
  constructor(private elRef: ElementRef, private renderer: Renderer2) { }

  ngOnInit() {
    this.navCollapsed = true;
  }

  checkAuthentication() {
    return false;
  }

}
