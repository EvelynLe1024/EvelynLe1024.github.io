
$(document).ready(() => {

    $('.wrong').hide();
    $('.correct').hide();
   
    $('.hint-box').on('click', () => {
        $('.hint-text').slideToggle();
    })
    $('.wrong-answer-one').on('click', () => {
        $('.wrong-text-one').fadeOut();
        $('.wrong').show();
      }) 
      $('.wrong-answer-two').on('click', () => {
        $('.wrong-text-two').fadeOut();
        $('.wrong').show();
      }) 
      $('.wrong-answer-three').on('click', () => {
        $('.wrong-text-three').fadeOut();
        $('.wrong').show();
      }) 
      $('.correct-answer').on('click', () => {
        $('.wrong').hide();
        $('.correct').show();
        $('.wrong-text-one').fadeOut();
        $('.wrong-text-two').fadeOut();
        $('.wrong-text-three').fadeOut();
      })

      $('.explanation').hide();
        $('#ellen').on('click', () => {
          $('#explanation-one').slideToggle();
        })
        $('#yoky').on('click', () => {
          $('#explanation-two').slideToggle();
        })
        $('#grace').on('click', () => {
          $('#explanation-three').slideToggle();
        })
        $('#evelyn').on('click', () => {
          $('#explanation-four').slideToggle();
        })

        $('.reset').on('click', () => {
        $('.hint-text').hide();
        $('.wrong-text-one').show();
        $('.wrong-text-two').show();
        $('.wrong-text-three').show();
        $('.correct-answer').show();
        $('.correct').hide();
        $('.wrong').hide();
        $('.explanation').hide();
        }) 


    
      })














