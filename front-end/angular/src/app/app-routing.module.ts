import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BancoComponent } from './componentes/bancos/banco/banco.component';
import { GetDespesasComponent } from './componentes/despesas/get-despesas/get-despesas.component';
import { GetImovelComponent } from './componentes/imovel/get-imovel/get-imovel.component';
import { GetPropretarioComponent } from './componentes/propretario/get-propretario/get-propretario.component';
import { MenuComponent } from './componentes/menu/menu.component';
import { PostClienteComponent } from './componentes/clientes/post-cliente/post-cliente.component';
import { ClienteComponent } from './componentes/clientes/cliente/cliente.component';


const routes: Routes = [

  {path: '', redirectTo: 'menu', pathMatch: 'full'},

  {path: 'menu', component: MenuComponent},
  {path: 'get-imovel', component: GetImovelComponent},
  {path: 'get-despesas', component: GetDespesasComponent},
  {path: 'banco', component: BancoComponent},
  {path: 'post-cliente', component: PostClienteComponent},
  {path: 'cliente', component: ClienteComponent},
  {path: 'get-proprietario', component: GetPropretarioComponent},
  {path: 'post-proprietario', component: PostClienteComponent}




];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
