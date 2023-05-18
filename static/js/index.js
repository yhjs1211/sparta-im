function next_sentence() {
    if (now_sentence == 1) {
      now_sentence += 1
      $('#sentence1').hide()
      $('#sentence2').fadeIn(800)
    } else if (now_sentence == 2) {
      now_sentence += 1
      $('#sentence2').hide()
      $('#sentence3').fadeIn(800)
    } else if (now_sentence == 3) {
      now_sentence = 1
      $('#sentence3').hide()
      $('#sentence1').fadeIn(800)
    }
  }
  now_sentence = 1
  function previous_sentence() {
    if (now_sentence == 1) {
      now_sentence = 3
      $('#sentence1').hide()
      $('#sentence3').fadeIn(800)
    } else if (now_sentence == 3) {
      now_sentence -= 1
      $('#sentence3').hide()
      $('#sentence2').fadeIn(800)
    } else if (now_sentence == 2) {
      now_sentence -= 1
      $('#sentence2').hide()
      $('#sentence1').fadeIn(800)
    }
  }