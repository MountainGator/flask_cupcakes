import { Component, OnInit, Input } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { EditComponent } from 'src/app/dialogs/edit/edit.component';
import { ConfirmComponent } from 'src/app/dialogs/confirm/confirm.component';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.scss']
})
export class DetailComponent implements OnInit {
  @Input('cake') cake: any;
  constructor(private dialog: MatDialog, private api: ApiService) { }

  ngOnInit(): void {
  }

  editCake(id: number) {
    const newDialogRef: MatDialogRef<EditComponent> = this.dialog.open(EditComponent, {data: this.cake});
  }

  deleteCake(id: number) {
    const newDialogRef: MatDialogRef<ConfirmComponent> = this.dialog.open(ConfirmComponent);

    newDialogRef.afterClosed().subscribe((res: string) => {
      if(res === 'yes') {
        this.api.deleteCake(id).subscribe((res: any) => {
          console.log('deleted')
        }) 
      } else return
    })
  }
}
