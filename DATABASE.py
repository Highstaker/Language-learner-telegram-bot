#!/usr/bin/python3

import os.path

PICK_LANGUAGE_METADATA = {"Prompt" : "Choose a language", "Name" : "Language"}
PICK_TYPE_OF_WORDS = {"Prompt" : "Choose a type of words", "Name" : "Type of words"}
CONJUGATION_METADATA = {"Prompt" : "Which conjugation? Or irregular?", "Name" : "Conjugation"}
VERB_METADATA = {"Prompt" : "Which verb?", "Name" : "Verb"}
TENSE_METADATA = {"Prompt" : "Which tense?", "Name" : "Tense"}

DATABASE = { "_metadata" : PICK_LANGUAGE_METADATA

,"Spanish": { "_metadata" : PICK_TYPE_OF_WORDS

,"Verbs":{ "_metadata" : CONJUGATION_METADATA
,"Conjugation_1" : { "_metadata" : VERB_METADATA
,"bailar" : { "_metadata" : TENSE_METADATA
,"Presente" :[("yo","bailo"),("tu","bailas"), ("el/ella","baila"),("nosotros", "bailamos"),("vosotros", "bailáis") ,("ellos", "bailan")]
,"Pretérito_imperfecto":[("yo","bailaba"),("tu","bailabas"), ("el/ella","bailaba"),("nosotros", "bailábamos"),("vosotros", "bailabais") ,("ellos", "bailaban")]
,"Pretérito_simple": [("yo","bailé"),("tu","bailaste"), ("el/ella","bailó"),("nosotros", "bailamos"),("vosotros", "bailasteis") ,("ellos", "bailaron")]
,"Futuro" :[("yo","bailaré"),("tu","bailarás"), ("el/ella","bailará"),("nosotros", "bailaremos"),("vosotros", "bailaréis") ,("ellos", "bailarán")]
,"Potencial":[("yo","bailaría"),("tu","bailarías"), ("el/ella","bailaría"),("nosotros", "bailaríamos"),("vosotros", "bailaríais") ,("ellos", "bailarían")]
,"Presente_de_subjuntivo": [("yo","baile"),("tu","bailes"), ("el/ella","baile"),("nosotros", "bailemos"),("vosotros", "bailéis") ,("ellos", "bailen")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","bailara"),("tu","bailaras"), ("el/ella","bailara"),("nosotros", "bailáramos"),("vosotros", "bailarais") ,("ellos", "bailaran")]
,"Modo_imperativo_afirmativo":[("tu","baila"), ("usted","baile"),("nosotros", "bailemos"),("vosotros", "bailad") ,("ustedes", "bailen")]
,"Formas_no_personales":[ ("Gerundio","bailando"), ("Participio","bailado") ]

}
}
,"Conjugation_2" : { "_metadata" : VERB_METADATA
,"comer" : { "_metadata" : TENSE_METADATA
,"Presente" :[("yo","como"), ("tu","comes"),("el/ella", "come"),("nosotros", "comemos"), ("vosotros","coméis") ,("ellos", "comen")]
,"Pretérito_imperfecto":[("yo","comía"), ("tu","comías"),("el/ella", "comía"),("nosotros", "comíamos"), ("vosotros","comíais") ,("ellos", "comían")]
,"Pretérito_simple": [("yo","comí"), ("tu","comiste"),("el/ella", "comió"),("nosotros", "comimos"), ("vosotros","comisteis") ,("ellos", "comieron")]
,"Futuro" :[("yo","comeré"), ("tu","comerás"),("el/ella", "comerá"),("nosotros", "comeremos"), ("vosotros","comeréis") ,("ellos", "comerán")]
,"Potencial":[("yo","comería"), ("tu","comerías"),("el/ella", "comería"),("nosotros", "comeríamos"), ("vosotros","comeríais") ,("ellos", "comerían")]
,"Presente_de_subjuntivo": [("yo","coma"), ("tu","comas"),("el/ella", "coma"),("nosotros", "comamos"), ("vosotros","comáis") ,("ellos", "coman")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","comiera"), ("tu","comieras"),("el/ella", "comiera"),("nosotros", "comiéramos"), ("vosotros","comierais") ,("ellos", "comieran")]
,"Modo_imperativo_afirmativo": [("tu","come"), ("usted","coma"),("nosotros", "comamos"),("vosotros", "comed") ,("ustedes", "coman")]
,"Formas_no_personales":[ ("Gerundio","comiendo"), ("Participio","comido") ]
}
}
,"Conjugation_3" : { "_metadata" : VERB_METADATA
,"vivir" : { "_metadata" : TENSE_METADATA
,"Presente" :[("yo","vivo"), ("tu","vives"),("el/ella", "vive"),("nosotros", "vivimos"), ("vosotros","vivís") ,("ellos", "viven")]
,"Pretérito_imperfecto":[("yo","vivía"), ("tu","vivías"),("el/ella", "vivía"),("nosotros", "vivíamos"), ("vosotros","vivíais") ,("ellos", "vivían")]
,"Pretérito_simple": [("yo","viví"), ("tu","viviste"),("el/ella", "vivió"),("nosotros", "vivimos"), ("vosotros","vivisteis") ,("ellos", "vivieron")]
,"Futuro" :[("yo","viviré"), ("tu","vivirás"),("el/ella", "vivirá"),("nosotros", "viviremos"), ("vosotros","viviréis") ,("ellos", "vivirán")]
,"Potencial":[("yo","viviría"), ("tu","vivirías"),("el/ella", "viviría"),("nosotros", "viviríamos"), ("vosotros","viviríais") ,("ellos", "vivirían")]
,"Presente_de_subjuntivo": [("yo","viva"), ("tu","vivas"),("el/ella", "viva"),("nosotros", "vivamos"), ("vosotros","viváis") ,("ellos", "vivan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","viviera"), ("tu","vivieras"),("el/ella", "viviera"),("nosotros", "viviéramos"), ("vosotros","vivierais") ,("ellos", "vivieran")]
,"Modo_imperativo_afirmativo": [("tu","vive"), ("usted","viva"),("nosotros", "vivamos"),("vosotros", "vivid") ,("ustedes", "vivan")]
,"Formas_no_personales":[ ("Gerundio","viviendo"), ("Participio","vivido") ]
}
}

,"Irregular":{ "_metadata" : VERB_METADATA
,"ir" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","voy"), ("tu","vas"),("el/ella", "va"),("nosotros", "vamos"), ("vosotros","vais") ,("ellos", "van")]
,"Pretérito_imperfecto":[("yo","iba"), ("tu","ibas"),("el/ella", "iba"),("nosotros", "íbamos"), ("vosotros","ibais") ,("ellos", "iban")]
,"Pretérito_simple": [("yo","fui"), ("tu","fuiste"),("el/ella", "fue"),("nosotros", "fuimos"), ("vosotros","fuisteis") ,("ellos", "fueron")]
,"Futuro" :[("yo","iré"), ("tu","irás"),("el/ella", "irá"),("nosotros", "iremos"), ("vosotros","iréis") ,("ellos", "irán")]
,"Potencial":[("yo","iría"), ("tu","irías"),("el/ella", "iría"),("nosotros", "iríamos"), ("vosotros","iríais") ,("ellos", "irían")]
,"Presente_de_subjuntivo": [("yo","vaya"), ("tu","vayas"),("el/ella", "vaya"),("nosotros", "vayamos"), ("vosotros","vayáis") ,("ellos", "vayan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","fuera"), ("tu","fueras"),("el/ella", "fuera"),("nosotros", "fuéramos"), ("vosotros","fuerais") ,("ellos", "fueran")]
,"Modo_imperativo_afirmativo": [("tu","ve"), ("usted","vaya"),("nosotros", "vayamos"),("vosotros", "id") ,("ustedes", "vayan")]
,"Formas_no_personales":[ ("Gerundio","yendo"), ("Participio","ido") ]
}

,"ser" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","soy"), ("tu","eres"),("el/ella", "es"),("nosotros", "somos"), ("vosotros","sois") ,("ellos", "son")]
,"Pretérito_imperfecto":[("yo","era"), ("tu","eras"),("el/ella", "era"),("nosotros", "éramos"), ("vosotros","erais") ,("ellos", "eran")]
,"Pretérito_simple": [("yo","fui"), ("tu","fuiste"),("el/ella", "fue"),("nosotros", "fuimos"), ("vosotros","fuisteis") ,("ellos", "fueron")]
,"Futuro" :[("yo","seré"), ("tu","serás"),("el/ella", "será"),("nosotros", "seremos"), ("vosotros","seréis") ,("ellos", "serán")]
,"Potencial":[("yo","sería"), ("tu","serías"),("el/ella", "sería"),("nosotros", "seríamos"), ("vosotros","seríais") ,("ellos", "serían")]
,"Presente_de_subjuntivo": [("yo","sea"), ("tu","seas"),("el/ella", "sea"),("nosotros", "seamos"), ("vosotros","seáis") ,("ellos", "sean")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","fuera"), ("tu","fueras"),("el/ella", "fuera"),("nosotros", "fuéramos"), ("vosotros","fuerais") ,("ellos", "fueran")]
,"Modo_imperativo_afirmativo": [("tu","sé"), ("usted","sea"),("nosotros", "seamos"),("vosotros", "sed") ,("ustedes", "sean")]
,"Formas_no_personales":[ ("Gerundio","siendo"), ("Participio","sido") ]
}

,"estar" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","estoy"), ("tu","estás"),("el/ella", "está"),("nosotros", "estamos"), ("vosotros","estáis") ,("ellos", "están")]
,"Pretérito_imperfecto":[("yo","estaba"), ("tu","estabas"),("el/ella", "estaba"),("nosotros", "estábamos"), ("vosotros","estabais") ,("ellos", "estaban")]
,"Pretérito_simple": [("yo","estuve"), ("tu","estuviste"),("el/ella", "estuvo"),("nosotros", "estuvimos"), ("vosotros","estuvisteis") ,("ellos", "estuvieron")]
,"Futuro" :[("yo","estaré"), ("tu","estarás"),("el/ella", "estará"),("nosotros", "estaremos"), ("vosotros","estaréis") ,("ellos", "estarán")]
,"Potencial":[("yo","estaría"), ("tu","estarías"),("el/ella", "estaría"),("nosotros", "estaríamos"), ("vosotros","estaríais") ,("ellos", "estarían")]
,"Presente_de_subjuntivo": [("yo","esté"), ("tu","estés"),("el/ella", "esté"),("nosotros", "estemos"), ("vosotros","estéis") ,("ellos", "estén")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","estuviera"), ("tu","estuvieras"),("el/ella", "estuviera"),("nosotros", "estuviéramos"), ("vosotros","estuvierais") ,("ellos", "estuvieran")]
,"Modo_imperativo_afirmativo": [("tu","está"), ("usted","esté"),("nosotros", "estemos"),("vosotros", "estad") ,("ustedes", "estén")]
,"Formas_no_personales":[ ("Gerundio","estando"), ("Participio","estado") ]
}

,"hacer" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","hago"), ("tu","haces"),("el/ella", "hace"),("nosotros", "hacemos"), ("vosotros","hacéis") ,("ellos", "hacen")]
,"Pretérito_imperfecto":[("yo","hacía"), ("tu","hacías"),("el/ella", "hacía"),("nosotros", "hacíamos"), ("vosotros","hacíais") ,("ellos", "hacían")]
,"Pretérito_simple": [("yo","hice"), ("tu","hiciste"),("el/ella", "hizo"),("nosotros", "hicimos"), ("vosotros","hicisteis") ,("ellos", "hicieron")]
,"Futuro" :[("yo","haré"), ("tu","harás"),("el/ella", "hará"),("nosotros", "haremos"), ("vosotros","haréis") ,("ellos", "harán")]
,"Potencial":[("yo","haría"), ("tu","harías"),("el/ella", "haría"),("nosotros", "haríamos"), ("vosotros","haríais") ,("ellos", "harían")]
,"Presente_de_subjuntivo": [("yo","haga"), ("tu","hagas"),("el/ella", "haga"),("nosotros", "hagamos"), ("vosotros","hagáis") ,("ellos", "hagan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","hiciera"), ("tu","hicieras"),("el/ella", "hiciera"),("nosotros", "hiciéramos"), ("vosotros","hicierais") ,("ellos", "hicieran")]
,"Modo_imperativo_afirmativo": [("tu","haz"), ("usted","haga"),("nosotros", "hagamos"),("vosotros", "haced") ,("ustedes", "hagan")]
,"Formas_no_personales":[ ("Gerundio","haciendo"), ("Participio","hecho") ]
}

,"tener" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","tengo"), ("tu","tienes"),("el/ella", "tiene"),("nosotros", "tenemos"), ("vosotros","tenéis") ,("ellos", "tienen")]
,"Pretérito_imperfecto":[("yo","tenía"), ("tu","tenías"),("el/ella", "tenía"),("nosotros", "teníamos"), ("vosotros","teníais") ,("ellos", "tenían")]
,"Pretérito_simple": [("yo","tuve"), ("tu","tuviste"),("el/ella", "tuvo"),("nosotros", "tuvimos"), ("vosotros","tuvisteis") ,("ellos", "tuvieron")]
,"Futuro" :[("yo","tendré"), ("tu","tendrás"),("el/ella", "tendrá"),("nosotros", "tendremos"), ("vosotros","tendréis") ,("ellos", "tendrán")]
,"Potencial":[("yo","tendría"), ("tu","tendrías"),("el/ella", "tendría"),("nosotros", "tendríamos"), ("vosotros","tendríais") ,("ellos", "tendrían")]
,"Presente_de_subjuntivo": [("yo","tenga"), ("tu","tengas"),("el/ella", "tenga"),("nosotros", "tengamos"), ("vosotros","tengáis") ,("ellos", "tengan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","tuviera"), ("tu","tuvieras"),("el/ella", "tuviera"),("nosotros", "tuviéramos"), ("vosotros","tuvierais") ,("ellos", "tuvieran")]
,"Modo_imperativo_afirmativo": [("tu","ten"), ("usted","tenga"),("nosotros", "tengamos"),("vosotros", "tened") ,("ustedes", "tengan")]
,"Formas_no_personales":[ ("Gerundio","teniendo"), ("Participio","tenido") ]
}

,"poder" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","puedo"), ("tu","puedes"),("el/ella", "puede"),("nosotros", "podemos"), ("vosotros","podéis") ,("ellos", "pueden")]
,"Pretérito_imperfecto":[("yo","podía"), ("tu","podías"),("el/ella", "podía"),("nosotros", "podíamos"), ("vosotros","podíais") ,("ellos", "podían")]
,"Pretérito_simple": [("yo","pude"), ("tu","pudiste"),("el/ella", "pudo"),("nosotros", "pudimos"), ("vosotros","pudisteis") ,("ellos", "pudieron")]
,"Futuro" :[("yo","podré"), ("tu","podrás"),("el/ella", "podrá"),("nosotros", "podremos"), ("vosotros","podréis") ,("ellos", "podrán")]
,"Potencial":[("yo","podría"), ("tu","podrías"),("el/ella", "podría"),("nosotros", "podríamos"), ("vosotros","podríais") ,("ellos", "podrían")]
,"Presente_de_subjuntivo": [("yo","pueda"), ("tu","puedas"),("el/ella", "pueda"),("nosotros", "podamos"), ("vosotros","podáis") ,("ellos", "puedan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","pudiera"), ("tu","pudieras"),("el/ella", "pudiera"),("nosotros", "pudiéramos"), ("vosotros","pudierais") ,("ellos", "pudieran")]
,"Modo_imperativo_afirmativo": [("tu","puede"), ("usted","pueda"),("nosotros", "podamos"),("vosotros", "poded") ,("ustedes", "puedan")]
,"Formas_no_personales":[ ("Gerundio","pudiendo"), ("Participio","podido") ]
}

,"decir" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","digo"), ("tu","dices"),("el/ella", "dice"),("nosotros", "decimos"), ("vosotros","decís") ,("ellos", "dicen")]
,"Pretérito_imperfecto":[("yo","decía"), ("tu","decías"),("el/ella", "decía"),("nosotros", "decíamos"), ("vosotros","decíais") ,("ellos", "decían")]
,"Pretérito_simple": [("yo","dije"), ("tu","dijiste"),("el/ella", "dijo"),("nosotros", "dijimos"), ("vosotros","dijisteis") ,("ellos", "dijeron")]
,"Futuro" :[("yo","diré"), ("tu","dirás"),("el/ella", "dirá"),("nosotros", "diremos"), ("vosotros","diréis") ,("ellos", "dirán")]
,"Potencial":[("yo","diría"), ("tu","dirías"),("el/ella", "diría"),("nosotros", "diríamos"), ("vosotros","diríais") ,("ellos", "dirían")]
,"Presente_de_subjuntivo": [("yo","diga"), ("tu","digas"),("el/ella", "diga"),("nosotros", "digamos"), ("vosotros","digáis") ,("ellos", "digan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","dijera"), ("tu","dijeras"),("el/ella", "dijera"),("nosotros", "dijéramos"), ("vosotros","dijerais") ,("ellos", "dijeran")]
,"Modo_imperativo_afirmativo": [("tu","di"), ("usted","diga"),("nosotros", "digamos"),("vosotros", "decid") ,("ustedes", "digan")]
,"Formas_no_personales":[ ("Gerundio","diciendo"), ("Participio","dicho") ]
}

,"ver" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","veo"), ("tu","ves"),("el/ella", "ve"),("nosotros", "vemos"), ("vosotros","veis") ,("ellos", "ven")]
,"Pretérito_imperfecto":[("yo","veía"), ("tu","veías"),("el/ella", "veía"),("nosotros", "veíamos"), ("vosotros","veíais") ,("ellos", "veían")]
,"Pretérito_simple": [("yo","vi"), ("tu","viste"),("el/ella", "vio"),("nosotros", "vimos"), ("vosotros","visteis") ,("ellos", "vieron")]
,"Futuro" :[("yo","veré"), ("tu","verás"),("el/ella", "verá"),("nosotros", "veremos"), ("vosotros","veréis") ,("ellos", "verán")]
,"Potencial":[("yo","vería"), ("tu","verías"),("el/ella", "vería"),("nosotros", "veríamos"), ("vosotros","veríais") ,("ellos", "verían")]
,"Presente_de_subjuntivo": [("yo","vea"), ("tu","veas"),("el/ella", "vea"),("nosotros", "veamos"), ("vosotros","veáis") ,("ellos", "vean")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","viera"), ("tu","vieras"),("el/ella", "viera"),("nosotros", "viéramos"), ("vosotros","vierais") ,("ellos", "vieran")]
,"Modo_imperativo_afirmativo": [("tu","ve"), ("usted","vea"),("nosotros", "veamos"),("vosotros", "ved") ,("ustedes", "vean")]
,"Formas_no_personales":[ ("Gerundio","viendo"), ("Participio","visto") ]
}

,"dar" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","doy"), ("tu","das"),("el/ella", "da"),("nosotros", "damos"), ("vosotros","dais") ,("ellos", "dan")]
,"Pretérito_imperfecto":[("yo","daba"), ("tu","dabas"),("el/ella", "daba"),("nosotros", "dabamos"), ("vosotros","dabais") ,("ellos", "daban")]
,"Pretérito_simple": [("yo","di"), ("tu","diste"),("el/ella", "dio"),("nosotros", "dimos"), ("vosotros","disteis") ,("ellos", "dieron")]
,"Futuro" :[("yo","daré"), ("tu","darás"),("el/ella", "dará"),("nosotros", "daremos"), ("vosotros","daréis") ,("ellos", "darán")]
,"Potencial":[("yo","daría"), ("tu","darías"),("el/ella", "daría"),("nosotros", "daríamos"), ("vosotros","daríais") ,("ellos", "darían")]
,"Presente_de_subjuntivo": [("yo","dé"), ("tu","des"),("el/ella", "dé"),("nosotros", "demos"), ("vosotros","deis") ,("ellos", "den")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","diera"), ("tu","dieras"),("el/ella", "diera"),("nosotros", "diéramos"), ("vosotros","dierais") ,("ellos", "dieran")]
,"Modo_imperativo_afirmativo": [("tu","da"), ("usted","dé"),("nosotros", "demos"),("vosotros", "dad") ,("ustedes", "den")]
,"Formas_no_personales":[ ("Gerundio","dando"), ("Participio","dado") ]
}

,"saber" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","sé"), ("tu","sabes"),("el/ella", "sabe"),("nosotros", "sabemos"), ("vosotros","sabéis") ,("ellos", "saben")]
,"Pretérito_imperfecto":[("yo","sabía"), ("tu","sabías"),("el/ella", "sabía"),("nosotros", "sabíamos"), ("vosotros","sabíais") ,("ellos", "sabían")]
,"Pretérito_simple": [("yo","supe"), ("tu","supiste"),("el/ella", "supo"),("nosotros", "supimos"), ("vosotros","supisteis") ,("ellos", "supieron")]
,"Futuro" :[("yo","sabré"), ("tu","sabrás"),("el/ella", "sabrá"),("nosotros", "sabremos"), ("vosotros","sabréis") ,("ellos", "sabrán")]
,"Potencial":[("yo","sabría"), ("tu","sabrías"),("el/ella", "sabría"),("nosotros", "sabríamos"), ("vosotros","sabríais") ,("ellos", "sabrían")]
,"Presente_de_subjuntivo": [("yo","sepa"), ("tu","sepas"),("el/ella", "sepa"),("nosotros", "sepamos"), ("vosotros","sepáis") ,("ellos", "sepan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","supiera"), ("tu","supieras"),("el/ella", "supiera"),("nosotros", "supiéramos"), ("vosotros","supierais") ,("ellos", "supieran")]
,"Modo_imperativo_afirmativo": [("tu","sabe"), ("usted","sepa"),("nosotros", "sepamos"),("vosotros", "sabed") ,("ustedes", "sepan")]
,"Formas_no_personales":[ ("Gerundio","sabiendo"), ("Participio","sabido") ]
}

,"querer" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","quiero"), ("tu","quieres"),("el/ella", "quiere"),("nosotros", "queremos"), ("vosotros","queréis") ,("ellos", "quieren")]
,"Pretérito_imperfecto":[("yo","quería"), ("tu","querías"),("el/ella", "quería"),("nosotros", "queríamos"), ("vosotros","queríais") ,("ellos", "querían")]
,"Pretérito_simple": [("yo","quise"), ("tu","quisiste"),("el/ella", "quiso"),("nosotros", "quisimos"), ("vosotros","quisisteis") ,("ellos", "quisieron")]
,"Futuro" :[("yo","querré"), ("tu","querrás"),("el/ella", "querrá"),("nosotros", "querremos"), ("vosotros","querréis") ,("ellos", "querrán")]
,"Potencial":[("yo","querría"), ("tu","querrías"),("el/ella", "querría"),("nosotros", "querríamos"), ("vosotros","querríais") ,("ellos", "querrían")]
,"Presente_de_subjuntivo": [("yo","quiera"), ("tu","quieras"),("el/ella", "quiera"),("nosotros", "queramos"), ("vosotros","queráis") ,("ellos", "quieran")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","quisiera"), ("tu","quisieras"),("el/ella", "quisiera"),("nosotros", "quisiéramos"), ("vosotros","quisierais") ,("ellos", "quisieran")]
,"Modo_imperativo_afirmativo": [("tu","quiere"), ("usted","quiera"),("nosotros", "queramos"),("vosotros", "quered") ,("ustedes", "quieran")]
,"Formas_no_personales":[ ("Gerundio","queriendo"), ("Participio","querido") ]
}

,"poner" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","pongo"), ("tu","pones"),("el/ella", "pone"),("nosotros", "ponemos"), ("vosotros","ponéis") ,("ellos", "ponen")]
,"Pretérito_imperfecto":[("yo","ponía"), ("tu","ponías"),("el/ella", "ponía"),("nosotros", "poníamos"), ("vosotros","poníais") ,("ellos", "ponían")]
,"Pretérito_simple": [("yo","puse"), ("tu","pusiste"),("el/ella", "puso"),("nosotros", "pusimos"), ("vosotros","pusisteis") ,("ellos", "pusieron")]
,"Futuro" :[("yo","pondré"), ("tu","pondrás"),("el/ella", "pondrá"),("nosotros", "pondremos"), ("vosotros","pondréis") ,("ellos", "pondrán")]
,"Potencial":[("yo","pondría"), ("tu","pondrías"),("el/ella", "pondría"),("nosotros", "pondríamos"), ("vosotros","pondríais") ,("ellos", "pondrían")]
,"Presente_de_subjuntivo": [("yo","ponga"), ("tu","pongas"),("el/ella", "ponga"),("nosotros", "pongamos"), ("vosotros","pongáis") ,("ellos", "pongan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","pusiera"), ("tu","pusieras"),("el/ella", "pusiera"),("nosotros", "pusiéramos"), ("vosotros","pusierais") ,("ellos", "pusieran")]
,"Modo_imperativo_afirmativo": [("tu","pon"), ("usted","ponga"),("nosotros", "pongamos"),("vosotros", "poned") ,("ustedes", "pongan")]
,"Formas_no_personales":[ ("Gerundio","poniendo"), ("Participio","puesto") ]
}

,"oír" : {"_metadata" : TENSE_METADATA
,"Presente" :[("yo","oigo"), ("tu","oyes"),("el/ella", "oye"),("nosotros", "oímos"), ("vosotros","oís") ,("ellos", "oyen")]
,"Pretérito_imperfecto":[("yo","oía"), ("tu","oías"),("el/ella", "oía"),("nosotros", "oíamos"), ("vosotros","oíais") ,("ellos", "oían")]
,"Pretérito_simple": [("yo","oí"), ("tu","oíste"),("el/ella", "oyó"),("nosotros", "oímos"), ("vosotros","oísteis") ,("ellos", "oyeron")]
,"Futuro" :[("yo","oiré"), ("tu","oirás"),("el/ella", "oirá"),("nosotros", "oiremos"), ("vosotros","oiréis") ,("ellos", "oirán")]
,"Potencial":[("yo","oiría"), ("tu","oirías"),("el/ella", "oiría"),("nosotros", "oiríamos"), ("vosotros","oiríais") ,("ellos", "oirían")]
,"Presente_de_subjuntivo": [("yo","oiga"), ("tu","oigas"),("el/ella", "oiga"),("nosotros", "oigamos"), ("vosotros","oigáis") ,("ellos", "oigan")]
,"Preterito_imperfecto_de_subjuntivo":[("yo","oyera"), ("tu","oyeras"),("el/ella", "oyera"),("nosotros", "oyéramos"), ("vosotros","oyerais") ,("ellos", "oyeran")]
,"Modo_imperativo_afirmativo": [("tu","oye"), ("usted","oiga"),("nosotros", "oigamos"),("vosotros", "oíd") ,("ustedes", "oigan")]
,"Formas_no_personales":[ ("Gerundio","oyendo"), ("Participio","oído") ]
}

}
}
}
}