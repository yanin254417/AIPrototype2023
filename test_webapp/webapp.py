<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>WebApp!</title>
  <style>
    body {
      background-image: url("https://t3.ftcdn.net/jpg/05/30/85/72/360_F_530857261_rZma7PhxiDQKDWCQXc7T3oBAKLaLtaB2.jpg");
      background-repeat: repeat-x;
      background-size: cover;
    }
  </style>
</head>

<body>
  <div ng-app="app">
    <div ng-controller="UploadController as vm">
      <div class="container">
        <div class="page-header">
          <h1><font style="color:hsl(329, 64%, 35%)"><font style="font-size: 25px;"><strong>WebApp!.</strong></font></font></h3>
        </div>
  
      
        <form action="{{ url_for('upload_file')}}" method="post">
        <!-- <form ng-model="vm.file" my-file-upload> -->
          <div class="form-group">
            <!-- <label for="fileName"><strong>Select a file</strong><br></label> -->
            <div class="input-group">
              <!-- <input type="file" id="fileName" class="form-control" readonly ng-model="fileName" ng-click="browse()">
              <span class="input-group-btn">
                <button type="button" class="btn btn-default" ng-click="browse()"class="text-center">Browse</button>
              </span> -->
              
            <label for="myfile"><font style="color:#b91a6e"><font style="font-size: 20px;"><strong>Upload file:   </strong></font></font></label>
            <strong><input type="file" id="myfile" 
            name="myfile" multiple="multiple"></strong>
            <br></br>
            
            <!-- <input id="hidden-input" type="file" name="images" multiple class="hidden" />
            <button id="button" type="button" class="mt-2 rounded-sm px-3 py-1 bg-gray-200 hover:bg-gray-300 focus:shadow-outline focus:outline-none">
              <strong>Upload a file</strong>
            </button> -->

            </div>
          </div>

    </div>
  </div>
</div>
</form>
</body>
</html>

<!--<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<main class="main_full">
	<div class="container">
		<div class="panel">
			<div class="button_outer">
				<div class="btn_upload">
					<input type="file" id="upload_file" name="">
					Upload Image
				</div>
				<div class="processing_bar"></div>
				<div class="success_box"></div>
			</div>
		</div>
		<div class="error_msg"></div>
		<div class="uploaded_file_view" id="uploaded_view">
			<span class="file_remove">X</span>
		</div>
	</div>
</main>-->


