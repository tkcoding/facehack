import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-face2',
  templateUrl: './face2.component.html',
  styleUrls: ['./face2.component.css']
})
export class Face2Component implements OnInit {
  myHeaders: { [name: string]: any } = {
    'Content-type': 'application/octet-stream',
    'X-Access-Token': 'fGF1DfdEWCeTaAqAdEsHXY0MMuo92avXuOhL'
  };
  constructor() { }

  ngOnInit() {

  }

  dostuff2() {

    var fileInput = document.getElementById("input1") as HTMLInputElement;
    console.log(fileInput)
    var files = fileInput.files;
    console.log(files);

    var xhr = new XMLHttpRequest();
    var result
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        result = xhr.responseText;
        console.log('success!!')
        console.log(result);
      }
    }

    xhr.open("POST", "https://dev.sighthoundapi.com/v1/detections?type=face,person&faceOption=landmark,gender");
    xhr.setRequestHeader("Content-type", "application/octet-stream");
    xhr.setRequestHeader("X-Access-Token", "fGF1DfdEWCeTaAqAdEsHXY0MMuo92avXuOhL");
    xhr.send(files[0]);
  }// dostuff2 end

}
