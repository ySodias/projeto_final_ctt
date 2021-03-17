import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BancoComponent } from './componentes/bancos/banco/banco.component';
import { ClienteComponent } from './componentes/clientes/cliente/cliente.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { PostClienteComponent } from './componentes/clientes/post-cliente/post-cliente.component';
import { PostBancoComponent } from './componentes/bancos/post-banco/post-banco.component';
import { GetBancoComponent } from './componentes/bancos/get-banco/get-banco.component';
import { RodapeComponent } from './componentes/rodape/rodape.component';
import { GetImovelComponent } from './componentes/imovel/get-imovel/get-imovel.component';
import { GetPropretarioComponent } from './componentes/propretario/get-propretario/get-propretario.component';
import { GetDespesasComponent } from './componentes/despesas/get-despesas/get-despesas.component';
import { MenuComponent } from './componentes/menu/menu.component';
import { NavBarComponent } from './componentes/nav-bar/nav-bar.component';
import { PostProprietarioComponent } from './componentes/propretario/post-proprietario/post-proprietario.component';



@NgModule({
  declarations: [
    AppComponent,
    BancoComponent,
    ClienteComponent,
    PostClienteComponent,
    PostBancoComponent,
    GetBancoComponent,
    RodapeComponent,
    GetImovelComponent,
    GetPropretarioComponent,
    GetDespesasComponent,
    MenuComponent,
    NavBarComponent,
    PostProprietarioComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
