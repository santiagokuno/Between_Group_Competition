
***********************************************************************************************
*** Between-group competition also enhances cooperation in public goods appropriation games ***
*** Experimental data 																		***
*** Collected between 06-12-2016 y el 08-24-2016 											***
***********************************************************************************************

** Base Treatment ***

{
import delimited "Base_session/Mlg Intro T0 (accessed 2016-08-24).csv", clear

gen aux_1 = substr(participanttime_started,1,19)
gen date_hour = clock(aux_1, "YMDhms")
format date_hour %tC
rename playerquestion playerquestion_1
gen question_1 = 1 if playerquestion_1 == 6.5
replace question_1 = 0 if playerquestion_1 != 6.5

keep participant_id_in_session date_hour participantcode playerquestion_1 sessioncode question_1

gen Treatment = 0

save Base_session/intro, replace

import delimited "Base_session/Cpr Game T1 (accessed 2016-08-24)", clear

keep participant_id_in_session participantcode playerid_in_group playerpayoff playerextraction ///
playerranking playergp_ranking groupid grouptotal_extraction ///
 grouptotal_payment subsessionround_number sessioncode

gen Treatment = 0 
gen Block = 1

save Base_session/B_1, replace

import delimited "Base_session/Cpr Game T2 (accessed 2016-08-24)", clear

keep participant_id_in_session participantcode playerid_in_group playerpayoff playerextraction ///
playerranking playergp_ranking groupid grouptotal_extraction ///
 grouptotal_payment subsessionround_number sessioncode

gen Treatment = 0 
gen Block = 2

save Base_session/B_2, replace

import delimited "Base_session/Cpr Game T3 (accessed 2016-08-24)", clear

keep participant_id_in_session participantcode playerid_in_group playerpayoff playerextraction ///
playerranking playergp_ranking groupid grouptotal_extraction ///
 grouptotal_payment subsessionround_number sessioncode

gen Treatment = 0 
gen Block = 3

save Base_session/B_3, replace

import delimited "Base_session/Mlg Survey (accessed 2016-08-24)", clear

keep participant_id_in_session participantcode playerq_age-playerp_trust_5 sessioncode

gen Treatment = 0 

save Base_session/Survey, replace

use Base_session/B_1, clear

append using Base_session/B_2
append using Base_session/B_3

merge m:1 participantcode sessioncode using Base_session/intro, keepusing(playerquestion_1 question_1 date_hour)
drop _merge
merge m:1 participantcode sessioncode using Base_session/Survey, keepusing(playerq_age-playerp_trust_5)
drop if _merge == 2
drop _merge
drop if sessioncode == "ntpyqyaq" // It correspond to a test session.

save Base_session/Data_T0.dta, replace
}

* 3 Groups Treatment
{
import delimited "T3_session/Mlg Intro (accessed 2016-08-24).csv", clear

gen aux_1 = substr(participanttime_started,1,19)
gen date_hour = clock(aux_1, "YMDhms")
format date_hour %tC
rename playerquestion playerquestion_1
gen question_1 = 1 if playerquestion_1 == 6.5
replace question_1 = 0 if playerquestion_1 != 6.5

keep participant_id_in_session date_hour participantcode playerquestion_1 sessioncode question_1

gen Treatment = 1

save T3_session/intro, replace

import delimited "T3_session/Cpr Game (accessed 2016-08-24)", clear

keep participant_id_in_session participantcode playerid_in_group playerpayoff playerextraction ///
playerranking playergp_ranking groupid grouptotal_extraction ///
 grouptotal_payment subsessionround_number sessioncode

gen Treatment = 1
gen Block = 1

save T3_session/B_1, replace

import delimited "T3_session/Mlg Change (accessed 2016-08-24)", clear

rename playerquestion_2 playerquestion_3
rename playerquestion_1 playerquestion_2
gen question_2 = 1 if playerquestion_2 == 6.5
replace question_2 = 0 if playerquestion_2 != 6.5
gen question_3 = 1 if playerquestion_3 > 6 & playerquestion_3 < 8 
replace question_3 = 0 if question_3 == .

keep participant_id_in_session participantcode playerquestion_2 playerquestion_3 sessioncode question_2 question_3

gen Treatment = 1

save T3_session/change, replace

import delimited "T3_session/Mlg Game (accessed 2016-08-24)", clear

keep participant_id_in_session participantcode playerid_in_group playerpayoff playerextraction playerpartial_pay ///
playerranking playergp_ranking groupid grouptotal_extraction ///
 grouptotal_payment subsessionround_number sessioncode

gen Treatment = 1 
gen Block = 2

save T3_session/B_2, replace

import delimited "T3_session/Mlg Change B (accessed 2016-08-24)", clear

rename playerquestion playerquestion_4

gen question_4 = 1 if playerquestion_4 == 6.5
replace question_4 = 0 if playerquestion_4 != 6.5

keep participant_id_in_session participantcode playerquestion_4 sessioncode question_4

gen Treatment = 1

save T3_session/change_b, replace

import delimited "T3_session/Cpr Game Ii (accessed 2016-08-24)", clear

keep participant_id_in_session participantcode playerid_in_group playerpayoff playerextraction ///
playerranking playergp_ranking groupid grouptotal_extraction ///
 grouptotal_payment subsessionround_number sessioncode

gen Treatment = 1 
gen Block = 3

save T3_session/B_3, replace

import delimited "T3_session/Mlg Survey (accessed 2016-08-24)", clear

keep participant_id_in_session participantcode playerq_age-playerp_trust_5 sessioncode

gen Treatment = 1 

save T3_session/Survey, replace

use T3_session/B_1, clear

append using T3_session/B_2
append using T3_session/B_3

merge m:1 participantcode sessioncode using T3_session/intro, keepusing(playerquestion_1 question_1 date_hour)
drop _merge

merge m:1 participantcode sessioncode using T3_session/change, keepusing(playerquestion_2 playerquestion_3 question_2 question_3)
drop _merge

merge m:1 participantcode sessioncode using T3_session/change_b, keepusing(playerquestion_4 question_4)
drop _merge

merge m:1 participantcode sessioncode using T3_session/Survey, keepusing(playerq_age-playerp_trust_5)
drop if _merge == 2
drop _merge

save T3_session/Data_T1.dta, replace
}

* 5 Group Treatment
{
import delimited "T5_session/Mlg Intro 5 (accessed 2016-08-23).csv", clear

gen aux_1 = substr(participanttime_started,1,19)
gen date_hour = clock(aux_1, "YMDhms")
format date_hour %tC
rename playerquestion playerquestion_1
gen question_1 = 1 if playerquestion_1 == 6.5
replace question_1 = 0 if playerquestion_1 != 6.5

keep participant_id_in_session date_hour participantcode playerquestion_1 sessioncode question_1

gen Treatment = 2

save T5_session/intro, replace

import delimited "T5_session/Cpr Game 5 (accessed 2016-08-23)", clear

keep participant_id_in_session participantcode playerid_in_group playerpayoff playerextraction ///
playerranking playergp_ranking groupid grouptotal_extraction ///
 grouptotal_payment subsessionround_number sessioncode

gen Treatment = 2
gen Block = 1

save T5_session/B_1, replace

import delimited "T5_session/Mlg Change 5 (accessed 2016-08-23)", clear

rename playerquestion_2 playerquestion_3
rename playerquestion_1 playerquestion_2
gen question_2 = 1 if playerquestion_2 == 6.5
replace question_2 = 0 if playerquestion_2 != 6.5
gen question_3 = 1 if playerquestion_3 > 6 & playerquestion_3 < 8 
replace question_3 = 0 if question_3 == .

keep participant_id_in_session participantcode playerquestion_2 playerquestion_3 sessioncode question_2 question_3

gen Treatment = 2

save T5_session/change, replace

import delimited "T5_session/Mlg Game 5 (accessed 2016-08-23)", clear

keep participant_id_in_session participantcode playerid_in_group playerpayoff playerextraction playerpartial_pay ///
playerranking playergp_ranking groupid grouptotal_extraction ///
 grouptotal_payment subsessionround_number sessioncode

gen Treatment = 2
gen Block = 2

save T5_session/B_2, replace

import delimited "T5_session/Mlg Change B (accessed 2016-08-23)", clear

rename playerquestion playerquestion_4

gen question_4 = 1 if playerquestion_4 == 6.5
replace question_4 = 0 if playerquestion_4 != 6.5

keep participant_id_in_session participantcode playerquestion_4 sessioncode question_4

gen Treatment = 2

save T5_session/change_b, replace

import delimited "T5_session/Cpr Game 5 Ii (accessed 2016-08-23)", clear

keep participant_id_in_session participantcode playerid_in_group playerpayoff playerextraction ///
playerranking playergp_ranking groupid grouptotal_extraction ///
 grouptotal_payment subsessionround_number sessioncode

gen Treatment = 2 
gen Block = 3

save T5_session/B_3, replace

import delimited "T5_session/Mlg Survey (accessed 2016-08-23)", clear

keep participant_id_in_session participantcode playerq_age-playerp_trust_5 sessioncode

gen Treatment = 2

save T5_session/Survey, replace

use T5_session/B_1, clear

append using T5_session/B_2
append using T5_session/B_3

merge m:1 participantcode sessioncode using T5_session/intro, keepusing(playerquestion_1 question_1 date_hour)
drop _merge

merge m:1 participantcode sessioncode using T5_session/change, keepusing(playerquestion_2 playerquestion_3 question_2 question_3)
drop _merge

merge m:1 participantcode sessioncode using T5_session/change_b, keepusing(playerquestion_4 question_4)
drop if _merge == 2
drop _merge

merge m:1 participantcode sessioncode using T5_session/Survey, keepusing(playerq_age-playerp_trust_5)
drop if _merge == 2
drop _merge


save T5_session/Data_T2.dta, replace
}

{

use "Base_session/Data_T0.dta", clear

append using "T3_session/Data_T1.dta"

append using "T5_session/Data_T2.dta"

rename (Treatment Block) (treatment block)
rename participant_id_in_session id_in_session
rename participantcode code_participant
rename playerid_in_group id_in_group
rename playerpayoff payoff
rename playerextraction extraction
rename playerrankin individual_ranking
rename playergp_ranking group_ranking
drop groupid
rename grouptotal_extraction group_extraction
rename grouptotal_payment group_payment
rename subsessionround_number round
rename sessioncode session
rename playerpartial_pay partial_pay
order playerq_age- playerp_trust_5, last
order partial_pay, after(payoff)
order session date_hour treatment block round, before(id_in_session)
order question_1 question_2 question_3 question_4, before(playerquestion_1)

label variable session "Codigo de la sesion"
label variable date_hour "Fecha y hora de inicio de cada jugador"
label variable treatment "Tratamiento para cada sesion: sin competencia, compt 3 grupos, compt 5 grupos"
label variable block "1o. 5 rondas, 2do. 10 rondas, 3o. 5 rondas"
label variable round "Ronda al interior del bloque"
label variable id_in_session "Nro de jugador en la sesion"
label variable code_participant "Codigo unico para cada participante"
label variable id_in_group "Nro de jugador en el grupo"
label variable payoff "Pago final en la ronda"
label variable partial_pay "Pago partial (solo si hay comp. entre grupos)"
label variable extraction "Decision de extraccion"
label variable individual_ranking "Ranking de jugadores"
label variable group_ranking "Ranking del grupo"
label variable group_extraction "Extraccion conjunta del grupo"
label variable group_payment "Suma de pagos parciales"
label variable question_1 "Evaluacion respuesta introduccion bloque 1"
label variable question_2 "Evalaucion respuesta 1 intro bloque 2"
label variable question_3 "Evaluacion respuesta 2 intro bloque 2"
label variable question_4 "Evaluacion respuesta intro bloque 3"
label variable playerquestion_1 "Respuesta introduccion bloque 1"
label variable playerquestion_2 "Respuesta 1 intro bloque 2"
label variable playerquestion_3 "Respuesta 2 intro bloque 2"
label variable playerquestion_4 "Respuesta intro bloque 3"

label define survey_1 1 "Absolutamente de acuerdo" 2 "De acuerdo" 3 "En desacuerdo" 4 "Muy en desacuerdo"
label define survey_2 3 "La nota sea individual" 2 "50% individual 50% grupo" 1 "Promedio del grupo"
label define survey_3 1 "la primera" 2 "la segunda"
label define survey_4 1 "Mi posicion individual" 2 "La posicion del grupo" 3 "Ambos igual de importantes"
label define answer 1 "Correcto" 0 "Incorrecto"
label define treat 0 "Sin competencia" 1 "Competencia 3 grupos" 2 "Competencia 5 grupos"

label variable playerq_age "ÀCual es su edad?"
label variable playerq_gender "ÀCual es su genero?"
label variable playerq_estrato "ÀCual es su estrato?"
label variable playerq_game_part "ÀHa participado en juegos similares a esta?"
label variable playerq_part_time "ÀEn cuantas actividades similares ha participado?"
label variable playerq_graduated "ÀEsta graduado de pregrado?"
label variable playerq_career_1 "ÀDe cual carrera 1?"
label variable playerq_career_2 "ÀDe cual carrera 2?"
label variable playerq_postgraduate "ÀEsta estudiando o se graduo de posgrado?"
label variable playerq_master_1 "ÀDe cual carrera de posgrado 1?"
label variable playerq_master_2 "ÀDe cual carrera de posgrado 2?"
label variable playerp_risk "Nivel de riesgo 1 nada, 10 mucho"
label variable playerp_compet_1 "Las notas deberian basarse en desempeno individual"
label variable playerp_compet_2 "El trabajo en grupo no es bueno porque permite free riders"
label variable playerp_compet_3 "El trabajo en grupo permite desarrollar habilidades para trabajar con otros"
label variable playerp_compet_4 "Las habilidades que mas se valoran en el mercado son las individuales"
label variable playerp_compet_5 "Me gustaria tener mas curso solo aprobado/no aprobado"
label variable playerp_compet_6 "En un trabajo en grupo como prefiero ser calificado"
label variable playerg_pref_stage "Cual etapa del juego le gusto mas"
label variable playerg_pref_rk_1 "En la primera etapa que informacion es mas importante"
label variable playerg_pref_rk_2 "En la segunda etapa que informacion es mas importante"
label variable playerg_pref_rk_3 "En la tercera etapa que informacion es mas importante"
label variable playerp_trust_1 "La mayor parte de las personas en la universidad son honestas y se puede confiar en ellas"
label variable playerp_trust_2 "Las personas en general en la universidad se preocupan por su propio beneficio"
label variable playerp_trust_3 "Se puede confiar mas en las personas en esta universidad que en otras universidades"
label variable playerp_trust_4 "En esta universidad hay que estar alerta, de otra manera alguien se puede aprovechar"
label variable playerp_trust_5 "En esta universidad si alguien tiene un problem, siempre hay alguien para ayudarlo"

label values playerp_compet_1 playerp_compet_2 playerp_compet_3 playerp_compet_4 playerp_compet_5 survey_1
label values playerp_compet_6 survey_2
label values playerg_pref_stage survey_3
label values playerg_pref_rk_1 playerg_pref_rk_2 playerg_pref_rk_3 survey_4
label values playerp_trust_1 playerp_trust_2 playerp_trust_3 playerp_trust_4 playerp_trust_5 survey_1
label values question_1 question_2 question_3 question_4 answer
label values treatment treat

gen round_cum = round 
replace round_cum = round + 5 if block == 2
replace round_cum = round + 15 if block == 3
order round_cum, after(round)

label variable round_cum "Ronda dentro de la sesion"

save Data_MLG.dta, replace
}


