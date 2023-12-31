import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  urlApi = 'http://127.0.0.1:8000/api/usuarios/'

  constructor(private http: HttpClient) { }

  getData(){
    return this.http.get<any>(this.urlApi)
  }
}
