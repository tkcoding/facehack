import { ItemsComponent } from './items/items.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule, PreloadAllModules } from '@angular/router';

const appRoutes: Routes = [
 { path: '', component: ItemsComponent },
 { path: 'items', component: ItemsComponent },
];

@NgModule({
 imports: [RouterModule.forRoot(appRoutes, {preloadingStrategy: PreloadAllModules})],
 exports: [RouterModule]
})
export class AppRoutingModule { }
