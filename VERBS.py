#!/usr/bin/python3

#TODO
#Add formas no personales

VERBS = {
"Conjugation_1" : {
"bailar" : { "Presente" :[("yo","bailo"),("tu","bailas"), ("el/ella","baila"),("nosotros", "bailamos"),("vosotros", "bailáis") ,("ellos", "bailan")]
,"Pretérito_imperfecto":[("yo","bailaba"),("tu","bailabas"), ("el/ella","bailaba"),("nosotros", "bailábamos"),("vosotros", "bailabais") ,("ellos", "bailaban")]
,"Pretérito_simple": [("yo","bailé"),("tu","bailaste"), ("el/ella","bailó"),("nosotros", "bailamos"),("vosotros", "bailasteis") ,("ellos", "bailaron")]
,"Futuro" :[("yo","bailaré"),("tu","bailarás"), ("el/ella","bailará"),("nosotros", "bailaremos"),("vosotros", "bailaréis") ,("ellos", "bailarán")]
,"Potencial":[("yo","bailaría"),("tu","bailarías"), ("el/ella","bailaría"),("nosotros", "bailaríamos"),("vosotros", "bailaríais") ,("ellos", "bailarían")]
,"Presente_de_subjuntivo": [("yo","baile"),("tu","bailes"), ("el/ella","baile"),("nosotros", "bailemos"),("vosotros", "bailéis") ,("ellos", "bailen")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","bailara"),("tu","bailaras"), ("el/ella","bailara"),("nosotros", "bailáramos"),("vosotros", "bailarais") ,("ellos", "bailaran")]
,"Modo_imperativo_afirmativo":[("tu","baila"), ("usted","baile"),("nosotros", "bailemos"),("vosotros", "bailad") ,("ustedes", "bailen")]
}
}
,"Conjugation_2" : {
"comer" : { "Presente" :[("yo","como"), ("tu","comes"),("el/ella", "come"),("nosotros", "comemos"), ("vosotros","coméis") ,("ellos", "comen")]
,"Pretérito_imperfecto":[("yo","comía"), ("tu","comías"),("el/ella", "comía"),("nosotros", "comíamos"), ("vosotros","comíais") ,("ellos", "comían")]
,"Pretérito_simple": [("yo","comí"), ("tu","comiste"),("el/ella", "comió"),("nosotros", "comimos"), ("vosotros","comisteis") ,("ellos", "comieron")]
,"Futuro" :[("yo","comeré"), ("tu","comerás"),("el/ella", "comerá"),("nosotros", "comeremos"), ("vosotros","comeréis") ,("ellos", "comerán")]
,"Potencial":[("yo","comería"), ("tu","comerías"),("el/ella", "comería"),("nosotros", "comeríamos"), ("vosotros","comeríais") ,("ellos", "comerían")]
,"Presente_de_subjuntivo": [("yo","coma"), ("tu","comas"),("el/ella", "coma"),("nosotros", "comamos"), ("vosotros","comáis") ,("ellos", "coman")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","comiera"), ("tu","comieras"),("el/ella", "comiera"),("nosotros", "comiéramos"), ("vosotros","comierais") ,("ellos", "comieran")]
,"Modo_imperativo_afirmativo": [("tu","come"), ("usted","coma"),("nosotros", "comamos"),("vosotros", "comed") ,("ustedes", "coman")]
}
}
,"Conjugation_3" : {
"vivir" : { "Presente" :[("yo","vivo"), ("tu","vives"),("el/ella", "vive"),("nosotros", "vivimos"), ("vosotros","vivís") ,("ellos", "viven")]
,"Pretérito_imperfecto":[("yo","vivía"), ("tu","vivías"),("el/ella", "vivía"),("nosotros", "vivíamos"), ("vosotros","vivíais") ,("ellos", "vivían")]
,"Pretérito_simple": [("yo","viví"), ("tu","viviste"),("el/ella", "vivió"),("nosotros", "vivimos"), ("vosotros","vivisteis") ,("ellos", "vivieron")]
,"Futuro" :[("yo","viviré"), ("tu","vivirás"),("el/ella", "vivirá"),("nosotros", "viviremos"), ("vosotros","viviréis") ,("ellos", "vivirán")]
,"Potencial":[("yo","viviría"), ("tu","vivirías"),("el/ella", "viviría"),("nosotros", "viviríamos"), ("vosotros","viviríais") ,("ellos", "vivirían")]
,"Presente_de_subjuntivo": [("yo","viva"), ("tu","vivas"),("el/ella", "viva"),("nosotros", "vivamos"), ("vosotros","viváis") ,("ellos", "vivan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","viviera"), ("tu","vivieras"),("el/ella", "viviera"),("nosotros", "viviéramos"), ("vosotros","vivierais") ,("ellos", "vivieran")]
,"Modo_imperativo_afirmativo": [("tu","vive"), ("usted","viva"),("nosotros", "vivamos"),("vosotros", "vivid") ,("ustedes", "vivan")]
}
}

,"Irregular":{
"ir" : {
 "Presente" :[("yo","voy"), ("tu","vas"),("el/ella", "va"),("nosotros", "vamos"), ("vosotros","vais") ,("ellos", "van")]
,"Pretérito_imperfecto":[("yo","iba"), ("tu","ibas"),("el/ella", "iba"),("nosotros", "íbamos"), ("vosotros","ibais") ,("ellos", "iban")]
,"Pretérito_simple": [("yo","fui"), ("tu","fuiste"),("el/ella", "fue"),("nosotros", "fuimos"), ("vosotros","fuisteis") ,("ellos", "fueron")]
,"Futuro" :[("yo","iré"), ("tu","irás"),("el/ella", "irá"),("nosotros", "iremos"), ("vosotros","iréis") ,("ellos", "irán")]
,"Potencial":[("yo","iría"), ("tu","irías"),("el/ella", "iría"),("nosotros", "iríamos"), ("vosotros","iríais") ,("ellos", "irían")]
,"Presente_de_subjuntivo": [("yo","vaya"), ("tu","vayas"),("el/ella", "vaya"),("nosotros", "vayamos"), ("vosotros","vayáis") ,("ellos", "vayan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","fuera"), ("tu","fueras"),("el/ella", "fuera"),("nosotros", "fuéramos"), ("vosotros","fuerais") ,("ellos", "fueran")]
,"Modo_imperativo_afirmativo": [("tu","ve"), ("usted","vaya"),("nosotros", "vayamos"),("vosotros", "id") ,("ustedes", "vayan")]
}

,"ser" : {
	"Presente" :[("yo","soy"), ("tu","eres"),("el/ella", "es"),("nosotros", "somos"), ("vosotros","sois") ,("ellos", "son")]
,"Pretérito_imperfecto":[("yo","era"), ("tu","eras"),("el/ella", "era"),("nosotros", "éramos"), ("vosotros","erais") ,("ellos", "eran")]
,"Pretérito_simple": [("yo","fui"), ("tu","fuiste"),("el/ella", "fue"),("nosotros", "fuimos"), ("vosotros","fuisteis") ,("ellos", "fueron")]
,"Futuro" :[("yo","seré"), ("tu","serás"),("el/ella", "será"),("nosotros", "seremos"), ("vosotros","seréis") ,("ellos", "serán")]
,"Potencial":[("yo","sería"), ("tu","serías"),("el/ella", "sería"),("nosotros", "seríamos"), ("vosotros","seríais") ,("ellos", "serían")]
,"Presente_de_subjuntivo": [("yo","sea"), ("tu","seas"),("el/ella", "sea"),("nosotros", "seamos"), ("vosotros","seáis") ,("ellos", "sean")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","fuera"), ("tu","fueras"),("el/ella", "fuera"),("nosotros", "fuéramos"), ("vosotros","fuerais") ,("ellos", "fueran")]
,"Modo_imperativo_afirmativo": [("tu","sé"), ("usted","sea"),("nosotros", "seamos"),("vosotros", "sed") ,("ustedes", "sean")]
}

,"estar" : {
	"Presente" :[("yo","estoy"), ("tu","estás"),("el/ella", "está"),("nosotros", "estamos"), ("vosotros","estáis") ,("ellos", "están")]
,"Pretérito_imperfecto":[("yo","estaba"), ("tu","estabas"),("el/ella", "estaba"),("nosotros", "estábamos"), ("vosotros","estabais") ,("ellos", "estaban")]
,"Pretérito_simple": [("yo","estuve"), ("tu","estuviste"),("el/ella", "estuvo"),("nosotros", "estuvimos"), ("vosotros","estuvisteis") ,("ellos", "estuvieron")]
,"Futuro" :[("yo","estaré"), ("tu","estarás"),("el/ella", "estará"),("nosotros", "estaremos"), ("vosotros","estaréis") ,("ellos", "estarán")]
,"Potencial":[("yo","estaría"), ("tu","estarías"),("el/ella", "estaría"),("nosotros", "estaríamos"), ("vosotros","estaríais") ,("ellos", "estarían")]
,"Presente_de_subjuntivo": [("yo","esté"), ("tu","estés"),("el/ella", "esté"),("nosotros", "estemos"), ("vosotros","estéis") ,("ellos", "estén")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","estuviera"), ("tu","estuvieras"),("el/ella", "estuviera"),("nosotros", "estuviéramos"), ("vosotros","estuvierais") ,("ellos", "estuvieran")]
,"Modo_imperativo_afirmativo": [("tu","está"), ("usted","esté"),("nosotros", "estemos"),("vosotros", "estad") ,("ustedes", "estén")]
}

,"hacer" : {
	"Presente" :[("yo","hago"), ("tu","haces"),("el/ella", "hace"),("nosotros", "hacemos"), ("vosotros","hacéis") ,("ellos", "hacen")]
,"Pretérito_imperfecto":[("yo","hacía"), ("tu","hacías"),("el/ella", "hacía"),("nosotros", "hacíamos"), ("vosotros","hacíais") ,("ellos", "hacían")]
,"Pretérito_simple": [("yo","hice"), ("tu","hiciste"),("el/ella", "hizo"),("nosotros", "hicimos"), ("vosotros","hicisteis") ,("ellos", "hicieron")]
,"Futuro" :[("yo","haré"), ("tu","harás"),("el/ella", "hará"),("nosotros", "haremos"), ("vosotros","haréis") ,("ellos", "harán")]
,"Potencial":[("yo","haría"), ("tu","harías"),("el/ella", "haría"),("nosotros", "haríamos"), ("vosotros","haríais") ,("ellos", "harían")]
,"Presente_de_subjuntivo": [("yo","haga"), ("tu","hagas"),("el/ella", "haga"),("nosotros", "hagamos"), ("vosotros","hagáis") ,("ellos", "hagan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","hiciera"), ("tu","hicieras"),("el/ella", "hiciera"),("nosotros", "hiciéramos"), ("vosotros","hicierais") ,("ellos", "hicieran")]
,"Modo_imperativo_afirmativo": [("tu","haz"), ("usted","haga"),("nosotros", "hagamos"),("vosotros", "haced") ,("ustedes", "hagan")]
}

,"tener" : {
	"Presente" :[("yo","tengo"), ("tu","tienes"),("el/ella", "tiene"),("nosotros", "tenemos"), ("vosotros","tenéis") ,("ellos", "tienen")]
,"Pretérito_imperfecto":[("yo","tenía"), ("tu","tenías"),("el/ella", "tenía"),("nosotros", "teníamos"), ("vosotros","teníais") ,("ellos", "tenían")]
,"Pretérito_simple": [("yo","tuve"), ("tu","tuviste"),("el/ella", "tuvo"),("nosotros", "tuvimos"), ("vosotros","tuvisteis") ,("ellos", "tuvieron")]
,"Futuro" :[("yo","tendré"), ("tu","tendrás"),("el/ella", "tendrá"),("nosotros", "tendremos"), ("vosotros","tendréis") ,("ellos", "tendrán")]
,"Potencial":[("yo","tendría"), ("tu","tendrías"),("el/ella", "tendría"),("nosotros", "tendríamos"), ("vosotros","tendríais") ,("ellos", "tendrían")]
,"Presente_de_subjuntivo": [("yo","tenga"), ("tu","tengas"),("el/ella", "tenga"),("nosotros", "tengamos"), ("vosotros","tengáis") ,("ellos", "tengan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","tuviera"), ("tu","tuvieras"),("el/ella", "tuviera"),("nosotros", "tuviéramos"), ("vosotros","tuvierais") ,("ellos", "tuvieran")]
,"Modo_imperativo_afirmativo": [("tu","ten"), ("usted","tenga"),("nosotros", "tengamos"),("vosotros", "tened") ,("ustedes", "tengan")]
}

,"poder" : {
	"Presente" :[("yo","puedo"), ("tu","puedes"),("el/ella", "puede"),("nosotros", "podemos"), ("vosotros","podéis") ,("ellos", "pueden")]
,"Pretérito_imperfecto":[("yo","podía"), ("tu","podías"),("el/ella", "podía"),("nosotros", "podíamos"), ("vosotros","podíais") ,("ellos", "podían")]
,"Pretérito_simple": [("yo","pude"), ("tu","pudiste"),("el/ella", "pudo"),("nosotros", "pudimos"), ("vosotros","pudisteis") ,("ellos", "pudieron")]
,"Futuro" :[("yo","podré"), ("tu","podrás"),("el/ella", "podrá"),("nosotros", "podremos"), ("vosotros","podréis") ,("ellos", "podrán")]
,"Potencial":[("yo","podría"), ("tu","podrías"),("el/ella", "podría"),("nosotros", "podríamos"), ("vosotros","podríais") ,("ellos", "podrían")]
,"Presente_de_subjuntivo": [("yo","pueda"), ("tu","puedas"),("el/ella", "pueda"),("nosotros", "podamos"), ("vosotros","podáis") ,("ellos", "puedan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","pudiera"), ("tu","pudieras"),("el/ella", "pudiera"),("nosotros", "pudiéramos"), ("vosotros","pudierais") ,("ellos", "pudieran")]
,"Modo_imperativo_afirmativo": [("tu","puede"), ("usted","pueda"),("nosotros", "podamos"),("vosotros", "poded") ,("ustedes", "puedan")]
}

,"decir" : {
	"Presente" :[("yo","digo"), ("tu","dices"),("el/ella", "dice"),("nosotros", "decimos"), ("vosotros","decís") ,("ellos", "dicen")]
,"Pretérito_imperfecto":[("yo","decía"), ("tu","decías"),("el/ella", "decía"),("nosotros", "decíamos"), ("vosotros","decíais") ,("ellos", "decían")]
,"Pretérito_simple": [("yo","dije"), ("tu","dijiste"),("el/ella", "dijo"),("nosotros", "dijimos"), ("vosotros","dijisteis") ,("ellos", "dijeron")]
,"Futuro" :[("yo","diré"), ("tu","dirás"),("el/ella", "dirá"),("nosotros", "diremos"), ("vosotros","diréis") ,("ellos", "dirán")]
,"Potencial":[("yo","diría"), ("tu","dirías"),("el/ella", "diría"),("nosotros", "diríamos"), ("vosotros","diríais") ,("ellos", "dirían")]
,"Presente_de_subjuntivo": [("yo","diga"), ("tu","digas"),("el/ella", "diga"),("nosotros", "digamos"), ("vosotros","digáis") ,("ellos", "digan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","dijera"), ("tu","dijeras"),("el/ella", "dijera"),("nosotros", "dijéramos"), ("vosotros","dijerais") ,("ellos", "dijeran")]
,"Modo_imperativo_afirmativo": [("tu","di"), ("usted","diga"),("nosotros", "digamos"),("vosotros", "decid") ,("ustedes", "digan")]
}

}
}
