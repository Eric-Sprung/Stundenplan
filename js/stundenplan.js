  $( function() {
  
//Auswahl der einzelnen HTML-Datein
 

//Fachbereich Informatik und digtitale Meiden//
 
	//Bachelor Informatik 
    $('#i_binf_1').click( function() {
	  $.get( "htm/INFB/1-1.htm", success, "HTML" );
    } );	

	$('#i_binf_2').click( function() {
      $.get( "htm/INFB/2-1.htm", success, "HTML" );
    } );

	$('#i_binf_3').click( function() {
      $.get( "htm/INFB/3-1.htm", success, "HTML" );
    } );
	
    $('#i_binf_4').click( function() {
	  $.get( "htm/INFB/4-1.htm", success, "HTML" );
    } );

	$('#i_binf_5').click( function() {
      $.get( "htm/INFB/5-1.htm", success, "HTML" );
    } );
	
	$('#i_binf_6').click( function() {
      $.get( "htm/INFB/6.htm", success, "HTML" );
    } );
	
	
	//Master Informatik 
	$('#i_minf_1').click( function() {
      $.get( "htm/INFM/1.htm", success, "HTML" );
    } );
	
	$('#i_minf_2').click( function() {
      $.get( "htm/INFM/2.htm", success, "HTML" );
    } );
	
	$('#i_minf_3').click( function() {
      $.get( "htm/INFM/3.htm", success, "HTML" );
    } );
	
	$('#i_minf_4').click( function() {
      $.get( "htm/INFM/4.htm", success, "HTML" );
    } );
	
	
	//Bachelor Medizininformatik
	$('#i_bmzi_1').click( function() {
      $.get( "htm/MEDI/1-1.htm", success, "HTML" );
    } );
	
	$('#i_bmzi_2').click( function() {
      $.get( "htm/MEDI/2-1.htm", success, "HTML" );
    } );

	$('#i_bmzi_3').click( function() {
      $.get( "htm/MEDI/3-1.htm", success, "HTML" );
    } );
	
	$('#i_bmzi_4').click( function() {
      $.get( "htm/MEDI/4-1.htm", success, "HTML" );
    } );

	$('#i_bmzi_5').click( function() {
      $.get( "htm/MEDI/5.htm", success, "HTML" );
    } );
	
	$('#i_bmzi_6').click( function() {
      $.get( "htm/MEDI/6.htm", success, "HTML" );
    } );
	
	
	//Bachelor Applied Computer Science 
	$('#i_bacs_1').click( function() {
      $.get( "htm/ACS/1-1.htm", success, "HTML" );
    } );
	
	$('#i_bacs_2').click( function() {
      $.get( "htm/ACS/2.htm", success, "HTML" );
    } );
	
	$('#i_bacs_3').click( function() {
      $.get( "htm/ACS/3.htm", success, "HTML" );
    } );
	
	$('#i_bacs_4').click( function() {
      $.get( "htm/ACS/4.htm", success, "HTML" );
    } );
	
	$('#i_bacs_5').click( function() {
      $.get( "htm/ACS/5.htm", success, "HTML" );
    } );
	
	$('#i_bacs_6').click( function() {
      $.get( "htm/ACS/6.htm", success, "HTML" );
    } );	
	
	
	//Master Digitale Medien
	$('#i_mdm_1').click( function() {
      $.get( "htm/DMM/1.htm", success, "HTML" );
    } );	
	
	$('#i_mdm_2').click( function() {
      $.get( "htm/DMM/2.htm", success, "HTML" );
    } );
	
	$('#i_mdm_3').click( function() {
      $.get( "htm/DMM/3.htm", success, "HTML" );
    } );
	
//Fachbereich Wirtschaft// 


	//Betriebswirtschaftslehre (Bachelor)
	$('#w_bbwl_1').click( function() {
      $.get( "htm/BWLB/1.Sem_1.Gr.htm", success, "HTML" );
    } );	
	
	$('#w_bbwl_2').click( function() {
      $.get( "htm/BWLB/2.Sem_1.Gr.htm", success, "HTML" );
    } );	
	
	$('#w_bbwl_3').click( function() {
      $.get( "htm/BWLB/3.Sem_1.Gr.htm", success, "HTML" );
    } );
	
	$('#w_bbwl_4').click( function() {
      $.get( "htm/BWLB/4.Sem_1.Gr.htm", success, "HTML" );
    } );

	$('#w_bbwl_5').click( function() {
      $.get( "htm/BWLB/5.Sem_1.Gr.htm", success, "HTML" );
    } );
	
	//Betriebswirtschaftslehre (Master)
	$('#w_mbwl_1').click( function() {
      $.get( "htm/BWLM/1.Sem_1.Gr.htm", success, "HTML" );
    } );
	
	$('#w_mbwl_2').click( function() {
      $.get( "htm/BWLM/2.Sem_1.Gr.htm", success, "HTML" );
    } );
	
	$('#w_mbwl_3').click( function() {
      $.get( "htm/BWLM/3.Sem_1.Gr.htm", success, "HTML" );
    } );
	
	//Wirtschaftsinformatik (Bachelor)
	$('#w_bwi_1').click( function() {
      $.get( "htm/WIB/1.Sem_1.Gr.htm", success, "HTML" );
    } );	
	
	$('#w_bwi_2').click( function() {
      $.get( "htm/WIB/2.Sem_1.Gr.htm", success, "HTML" );
    } );
	
	$('#w_bwi_3').click( function() {
      $.get( "htm/WIB/3.Sem_1.Gr.htm", success, "HTML" );
    } );	
	
	$('#w_bwi_4').click( function() {
      $.get( "htm/WIB/4.Sem_1.Gr.htm", success, "HTML" );
    } );

	$('#w_bwi_5').click( function() {
      $.get( "htm/WIB/5.Sem_1.Gr.htm", success, "HTML" );
    } );	
	
	//Wirtschaftsinformatik (Master)
	$('#w_mwi_1').click( function() {
      $.get( "htm/WIM/1.Sem_1.Gr.htm", success, "HTML" );
    } );	
	
	$('#w_mwi_2').click( function() {
      $.get( "htm/WIM/2.Sem_1.Gr.htm", success, "HTML" );
    } );
	
	$('#w_mwi_3').click( function() {
      $.get( "htm/WIM/3.Sem_1.Gr.htm", success, "HTML" );
    } );	

	//Security Management (Master)
	$('#w_msec_1').click( function() {
      $.get( "htm/SM/1.Sem.htm", success, "HTML" );
    } );	
	
	$('#w_msec_2').click( function() {
      $.get( "htm/SM/2.Sem.htm", success, "HTML" );
    } );

	$('#w_msec_3').click( function() {
      $.get( "htm/SM/3.Sem.htm", success, "HTML" );
    } );
	
	//Technologie- und Innovationsmanagement (Master)
	$('#w_mtim_1').click( function() {
      $.get( "htm/TIM/1.Sem.htm", success, "HTML" );
    } );
	
	$('#w_mtim_2').click( function() {
      $.get( "htm/TIM/2.Sem.htm", success, "HTML" );
    } );

	$('#w_mtim_3').click( function() {
      $.get( "htm/TIM/3.Sem.htm", success, "HTML" );
    } );	
	
//Fachbereich Technik//	

	//Augenoptik/Optische Gerätetechnik (Bachelor)
	$('#t_baog_1').click( function() {
      $.get( "htm/AOG/1.htm", success, "HTML" );
    } );	
	
	$('#t_baog_2').click( function() {
      $.get( "htm/AOG/2.htm", success, "HTML" );
    } );
	
	//Computer Aided Robust Engineering (Master), künftig Maschinenbau
	$('#t_mcare_1').click( function() {
      $.get( "htm/CARE/1.htm", success, "HTML" );
    } );
	
	$('#t_mcare_2').click( function() {
      $.get( "htm/CARE/2.htm", success, "HTML" );
    } );
	
	//Energieeffizienz Technischer Systeme (Master)
	$('#t_menef_1').click( function() {
      $.get( "htm/ENEF/1.htm", success, "HTML" );
    } );
	
	$('#t_menef_2').click( function() {
      $.get( "htm/ENEF/2.htm", success, "HTML" );
    } );
	
	$('#t_menef_3').click( function() {
      $.get( "htm/ENEF/3.htm", success, "HTML" );
    } );	
	
	//Elektronik (Bachelor)
	$('#t_bel_5').click( function() {
      $.get( "htm/BEL/5.htm", success, "HTML" );
    } );	
	
	$('#t_bel_6').click( function() {
      $.get( "htm/BEL/6.htm", success, "HTML" );
    } );
	
	$('#t_bel_7').click( function() {
      $.get( "htm/BEL/7.htm", success, "HTML" );
    } );
	
	//Ingenieurwissenschaften (Bachelor)
	$('#t_bingwis_1').click( function() {
      $.get( "htm/IW/1-1.htm", success, "HTML" );
    } );
	
	$('#t_bingwis_2').click( function() {
      $.get( "htm/IW/2-1.htm", success, "HTML" );
    } );
	
	$('#t_bingwis_3').click( function() {
      $.get( "htm/IW/3-1.htm", success, "HTML" );
    } );
	
	$('#t_bingwis_4').click( function() {
      $.get( "htm/IW/4-1.htm", success, "HTML" );
    } );
	
	//Maschinenbau (Bachelor)
	$('#t_bmb_1').click( function() {
      $.get( "htm/MB/1-1.htm", success, "HTML" );
    } );	
	
	$('#t_bmb_2').click( function() {
      $.get( "htm/MB/2-1.htm", success, "HTML" );
    } );
	
	$('#t_bmb_3').click( function() {
      $.get( "htm/MB/3-1-AM.htm", success, "HTML" );
    } );
	
	$('#t_bmb_4').click( function() {
      $.get( "htm/MB/4-1-AM.htm", success, "HTML" );
    } );
	
	$('#t_bmb_5').click( function() {
      $.get( "htm/MB/5-1-AM.htm", success, "HTML" );
    } );
	
	$('#t_bmb_6').click( function() {
      $.get( "htm/MB/6-1-AM.htm", success, "HTML" );
    } );

	$('#t_bmb_7').click( function() {
      $.get( "htm/MB/7-1-AM.htm", success, "HTML" );
    } );	
	
	//Mechatronik/Automatisierungssysteme (Bachelor)
	$('#t_bmt_5').click( function() {
      $.get( "htm/BMTAT/5-MT.htm", success, "HTML" );
    } );	
	
	$('#t_bmt_6').click( function() {
      $.get( "htm/BMTAT/6-MT.htm", success, "HTML" );
    } );
	
	$('#t_bmt_7').click( function() {
      $.get( "htm/BMTAT/7-MT.htm", success, "HTML" );
    } );	
	//Mikrosystemtechnik und Optische Technologien (Bachelor)
	$('#t_bmiopt_5').click( function() {
      $.get( "htm/MIOPT/5.htm", success, "HTML" );
    } );	
	
	$('#t_bmiopt_6').click( function() {
      $.get( "htm/MIOPT/6.htm", success, "HTML" );
    } );
	
	$('#t_bmiopt_7').click( function() {
      $.get( "htm/MIOPT/7.htm", success, "HTML" );
    } );
	
	//Photonics (Master)
	$('#t_mph_1').click( function() {
      $.get( "htm/PHT/1.htm", success, "HTML" );
    } );	
	
	$('#t_mph_2').click( function() {
      $.get( "htm/PHT/2.htm", success, "HTML" );
    } );
	
	$('#t_mph_3').click( function() {
      $.get( "htm/PHT/3.htm", success, "HTML" );
    } );	
	//Wirtschaftsingenieurwesen (Bachelor)
	$('#t_bwing_1').click( function() {
      $.get( "htm/WING/1-1.htm", success, "HTML" );
    } );	
	
	$('#t_bwing_2').click( function() {
      $.get( "htm/WING/1-2.htm", success, "HTML" );
    } );

	$('#t_bwing_3').click( function() {
      $.get( "htm/WING/1-3.htm", success, "HTML" );
    } );
	
	$('#t_bwing_4').click( function() {
      $.get( "htm/WING/1-4.htm", success, "HTML" );
    } );

	
	
	//Öffnen der HTML Datei im Div-Container "content"
    function success( forecastData ) {
    $('#content').html (forecastData) ;
    }
 
  } );