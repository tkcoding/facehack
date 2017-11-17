import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ImageUploadModule } from 'angular2-image-upload'

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { TopNavComponent } from './ui/top-nav/top-nav.component';
import { DropdownDirective } from './ui/dropdown.directive';
import { FooterComponent } from './ui/footer/footer.component';
import { ItemsComponent } from './items/items.component';
import { ItemsService } from './services/items.service';
import { FaceComponent } from './face/face.component';
import { Face2Component } from './face2/face2.component';

@NgModule({
  declarations: [
    AppComponent,
    TopNavComponent,
    DropdownDirective,
    FooterComponent,
    ItemsComponent,
    FaceComponent,
    Face2Component
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpModule,
    AppRoutingModule,
    ImageUploadModule.forRoot(),
    NgbModule.forRoot()
  ],
  providers: [ItemsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
