function stvoriNagradu(){
    $('.achievement-paneNagrada').children().css({opacity: 0});
    
    var middle = 0;
   
    $('.iconNagrada').animate({top: 0, left: 0, opacity: 1}, 100);
    $('.textNagrada').delay(1100).animate({top: 0, left: 0, opacity: 1}, 100);
    $('.achievement-pane').delay(700).animate({left: middle+'px'}, 100);
    $('.textNagrada').children().eq(0).delay(2500).animate({position: 'relative', left: '120%' });
    $('.textNagrada').children().eq(1).delay(2700).animate({position: 'relative', top: '-20px' });
    
      $('.iconNagrada').delay(4500).animate({top: '-20px', left: '-0px', opacity: 0}, 300);
    $('.textNagrada').delay(3700).animate({top: '-20px', left: '-0px', opacity: 0}, 300);
  };