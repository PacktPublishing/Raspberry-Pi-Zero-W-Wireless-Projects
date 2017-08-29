<html>
<head>
  <title>PI Zero W - Chatbot</title>
  <link rel="stylesheet" href="style.css" />
  <?php
    if( isset($_POST['usertext'])) {
      $input = $_POST['usertext'];
      switch($input) {
        case "hello":
          $outdata = "Hello there! What can I do for you?";
          break;
        case "hi":
            $outdata = "Hey! What' up?";
            break;
        case "how are you?":
          $outdata = "I am fine! You?";
          break;
        case "what time is it?":
            $timezone = date_default_timezone_get();
            date_default_timezone_set($timezone);
            $date = date('h:i:s a', time());
            $outdata = "The time is: " . $date;
            break;
        case "who are you?":
            $outdata = "I am your lovely chatbot!";
            break;    default:
        $outdata = "Oup's  I didn' t get that!";
          break;
      }
    }
  ?>
</head>
<body>
  <div id="header">
    Pi Zero W ChatBot v1.0
  </div>
  <div id="main">
    <form method="POST" action="">
      <input id="userinput" type="text" name="usertext" value="Type here...">
      <br><br>
      <input id="submitbutton" type="submit" value="Submit">
    </form>
    <div id="answer">
      ChatBot answer:<br><br><br>
      <?php
        if(!isset($outdata)) {
          echo "";
        }else {
          echo $outdata;
        }
      ?>
    </div>
  </div>
</body>
</html>
