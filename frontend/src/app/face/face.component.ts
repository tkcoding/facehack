import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-face',
  templateUrl: './face.component.html',
  styleUrls: ['./face.component.css']
})
export class FaceComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  onUploadFinished(file) {
    console.log('upload complete')
    console.log(file)
    console.log(JSON.stringify(file.serverResponse));
  }

  onRemoved(file) {
    // do some stuff with the removed file.
  }

  onUploadStateChanged(state: boolean) {
    console.log(JSON.stringify(state));
  }

  onBeforeUpload = (metadata) => {
    console.log('before upload')
    console.log(metadata);
    metadata.abort = false;
    metadata.test = "hello"
    console.log(metadata);
    return metadata;
  };
   
  fileChanged(e: Event) {
    var target: HTMLInputElement = e.target as HTMLInputElement;
    for (var i = 0; i < target.files.length; i++) {
      this.upload(target.files[i]);
    }
  }

  upload(img: File) {
    var formData: FormData = new FormData();
    formData.append("file", img, img.name);

    var xhr = new XMLHttpRequest();
    xhr.upload.addEventListener("progress", (ev: ProgressEvent) => {
      //You can handle progress events here if you want to track upload progress (I used an observable<number> to fire back updates to whomever called this upload)
    });
    xhr.open("POST", "https://localhost:5000/img", true);
    xhr.send(formData);
  }

}
