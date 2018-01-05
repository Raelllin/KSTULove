$(document).ready(function(){

  var clock;
  clock = $('.clock').FlipClock(){
    clockface : "DailyCounter",
    autostart : false,
    callbacks : {
      stop : function(){
        $('.sms').html('Время прошло!');
      }
    }
  }


clock.setTime(5000);
clock.setCounddown(true);
clock.start();
});


<div class="colour">
  <div class="clock"></div>
  <div class="sms"></div>
</div>



<div class="timer">
  <div class="timer-time">
    <div class="timer-items">
      <span class="timer-items-numbers" id="timer-hours"></span>
    </div>
    <div class="timer-items">
      <span class="timer-items-numbers" id="timer-minutes"></span>
    </div>
    <div class="timer-items">
      <span class="timer-items-numbers" id="timer-seconds"></span>
    </div>
  </div>
