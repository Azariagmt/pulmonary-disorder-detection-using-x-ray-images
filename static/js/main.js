$(document).ready(function () {
  // Init
  $(".image-section-one").hide();
  $(".image-section-two").hide();
  $(".loader-one").hide();
  $(".loader-two").hide();
  $("#result-one").hide();
  $("#result-two").hide();

  // Upload Preview
  function readURLone(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $("#imagePreviewOne").css(
          "background-image",
          "url(" + e.target.result + ")"
        );
        // $("#imagePreviewOne").hide();
        $("#imagePreviewOne").fadeIn(650);
      };
      reader.readAsDataURL(input.files[0]);
    }
  }
  $("#imageUploadOne").change(function () {
    $(".image-section-one").show();
    $("#btn-predict-one").show();
    $("#result-one").text("");
    $("#result-one").hide();
    readURLone(this);
  });
  function readURLtwo(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $("#imagePreviewTwo").css(
          "background-image",
          "url(" + e.target.result + ")"
        );
        // $("#imagePreviewTwo").hide();
        $("#imagePreviewTwo").fadeIn(650);
      };
      reader.readAsDataURL(input.files[0]);
    }
  }

  $("#imageUploadTwo").change(function () {
    $(".image-section-two").show();
    $("#btn-predict-two").show();
    $("#result-two").text("");
    $("#result-two").hide();
    readURLtwo(this);
  });

  // Predict
  $("#btn-predict-one").click(function () {
    var form_data = new FormData($("#upload-file-one")[0]);
    // Show loading animation
    $(this).hide();
    $(".loader-one").show();
    // Make prediction by calling api /predict
    $.ajax({
      beforeSend: function () {},
      type: "POST",
      url: "/predict/binary",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: true,
      success: function (data) {
        // Get and display the result
        $(".loader-one").hide();
        $("#result-one").fadeIn(600);
        console.log("data:", data);
        $("#result-one").text(" Result:  " + data);
        console.log("Success!");
      },
    });
  });

  $("#btn-predict-two").click(function () {
    var form_data = new FormData($("#upload-file-two")[0]);

    // Show loading animation
    $(this).hide();
    $(".loader-two").show();

    // Make prediction by calling api /predict
    $.ajax({
      beforeSend: function () {},
      type: "POST",
      url: "/predict/multiclass",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: true,
      success: function (data) {
        // Get and display the result
        $(".loader-two").hide();
        $("#result-two").fadeIn(600);
        console.log("data:", data);
        $("#result.two").text(" Result:  " + data);
        console.log("Success!");
      },
    });
  });
});
