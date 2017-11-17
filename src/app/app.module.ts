import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { TopNavComponent } from './ui/top-nav/top-nav.component';
import { DropdownDirective } from './ui/dropdown.directive';
import { FooterComponent } from './ui/footer/footer.component';
import { ItemsComponent } from './items/items.component';
import { ItemsService } from './services/items.service';

@NgModule({
  declarations: [
    AppComponent,
    TopNavComponent,
    DropdownDirective,
    FooterComponent,
    ItemsComponent
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpModule,
    AppRoutingModule,
    NgbModule.forRoot()
  ],
  providers: [ItemsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
