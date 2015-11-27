<?php
  require("template/header.php");

 ?>


<div class="container">
   <?php require("template/nav.php") ?>
   <div class="row">
     <div class="col-md-12">
       <div class="panel panel-default">
         <div class="panel-heading">
           <h3 class="panel-title">Remeo Dallaire Child Soldier Initiative - Country Reports</h3>
         </div>
         <div class="panel-body">
           <?php
              $json = file_get_contents('http://127.0.0.1:8000/countryreports/');
              $obj = json_decode($json, true);
              foreach ($obj as $value){
                print_r($value);
                echo '</br>';
                // $json1 = file_get_contents('http://127.0.0.1:8000/countryreports/'.$value[id]);
                // $obj1 = json_decode($json, true);
                echo 'http://127.0.0.1:8000/countryreports/'.$value[id];

                echo '</br>';
              }
            ?>
         </div>
         <div class="panel-footer">

         </div>
       </div>
     </div>
   </div>
</div>

<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<script src="js/bootstrap.min.js"></script>


<?php
  require("template/footer.php");
 ?>
