import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface cakePost {
  _id: number;
  flavor: | string | null;
  size: | string | null;
  rating: | number | null;
  image: | string | null;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) { }

  getAll (): Observable<any> {
    return this.http.get('/cupcakes')
  }

  getSingle (id: number): Observable<any> {
    return this.http.get('/cupcakes/' + id )
  }

  search(query: string): Observable<any> {
    return this.http.get('/cupcakes/search/' + query)
  }

  createCupcake (postBody: cakePost): Observable<any> {
    const res: any = this.http.post('/cupcakes', postBody);
    console.log('post response:', res);
    return res
  }

  updateCake (id: number, updateBody: cakePost): Observable<any> {
    const res: any = this.http.patch('/cupcakes/update/' + id, updateBody);
    console.log('post response:', res);
    return res
  }

  deleteCake (id: number): Observable<any> {
    return this.http.delete('/cupcakes/delete/' + id)
  }
}
