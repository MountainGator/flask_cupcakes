import { Component, OnInit, Inject } from '@angular/core';
import { cakePost } from 'src/app/services/api.service';
import { MatDialog, MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { ApiService } from 'src/app/services/api.service';

export interface DialogData<cakePost> {
  _id: number;
  flavor: | string | null;
  size: | string | null;
  rating: | number | null;
  image: | string | null;
}

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.scss']
})
export class EditComponent implements OnInit {

  constructor(@Inject(MAT_DIALOG_DATA) public data: DialogData<cakePost>, private api: ApiService, public dialogRef: MatDialogRef<EditComponent>) { }

  ngOnInit(): void {
  }

  editCake (id: number) {
    this.api.updateCake(id, this.data)
    this.dialogRef.close()
  }
}
