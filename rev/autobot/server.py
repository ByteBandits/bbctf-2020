#!/usr/bin/python2 -u
alphabets = [
'QEKLCPXRdcOrwWgpalmhysSkGMBVHz',
'FPTVhUxCJdjsASzoZaRlwpHDiMqBeL',
'IsDCWJgXHpdifbBzkPcUaytmxEOTuN',
'jzLRWdCKMZlPtyDsvuoFfqiHkBcOTJ',
'CjTGWcFXMqnSlIxiwEagDzhoKBVQpr',
'QhBFHIgECXVaqjpRKWonzJMsTteDbr',
'ChuzbFGnTJrxAWSHtdZDPlyqfvQYcw',
'fHkglXMwiVraBpCbKTeWLmsAREqndo',
'sTpoWhtAjIDxrMaBYkymvCSJXinqFZ',
'gEaLVDZjvSnkGwMOdesWPqyNoHYczm',
'FVyRjwtqAEkSTLfiXrlWpHoPCZmDsY',
'XnlpZrfctgAoQkuRKvqDTSjsPwJELO',
'TmHPIDFJsOkejdXEhqKYWVlpzAwMUQ',
'hCTfkcjLAqJQvBKVwYZxREWGnzIeNr',
'AEYsfoKgjWwlNIGDvtycPmpOQJuSkx',
'lkRbOcjGFoZiePLrxgUWQCmqyYXEuH',
'fqeguraSAYjxoXZlpbwzOPnkHCsBGJ',
'QYfWeXJODMvdVzSarEpsLxBhyTnFtP',
'svMojliDLTUdQZAuCmeKcprXxqByRN',
'tlWOUqKnSmbRhaFfeyJXIvuzNjwVgP',
'syUIeXFTRloKJwqMQbGZgEWxhtiaHC',
'VIgKqnDZWCSTQzNkYcaFBXpURPJdHs',
'jcgrTWZyakptqDBMIbwAYeQCvSKUNx',
'qUdgIONBKYmLDbnZleWpwaETMroscF',
'UBybsYXpANnfTaWckRjxgiSLDdGPhM',
'uAdZtRvIybHJSzXGDLeMCjkipVPFfw',
'ROMzuNnoxftGvygPCBDJKLXIjbYidm',
'XkevsuwqMtzCHdElbJTSPYAOFBjLWV',
'mXjFcBxDtAdovhMSnaIZLPpNWfyeOi',
'TuHsdJmQDibWMCReFpwkLNjlncxUzS',
'EvtAcVzgFsqTOkHIDLWSMUlBRaXryi',
'rBzCGcHNTbuLOUfwjvExIlKFmQgPsZ',
'QRtrymGJCwqouKBvFZcSDskNizeUlA',
'rywpYhGJBPCumiTHFNzkfLXIlstdWO',
'pCuqXmUxHIrBOPLJtlYghAdayenFRD',
'ZhUqcQCLBrDpYjyOPlxgNXoGzKnRtw',
'WsvFOiljepHDwLAmcJorkfRnIuKNYV',
'maWVqwtgeoKslzykJjLQuNTMbRIcCA',
'FjlhVrGgbumBUQpwtyfMJDZSPNiqTH',
'bgSUxIwBtHyFTMCrzeqNXKiAnWPsmG',
'gdJWChBrTEKajDiyoxUpIeXcYPfFOS',
'VbxhXtJgsfmaEWDUurGHRwTeiSAKpQ',
'hnrsZXopMtQyvdTSGYRJIDzOHKUexq',
'XPFHolZjamWUNuTtChQAkcYfEgIpSM',
'tEJwgBxacQTbjGzFrUCmZIlSuODdNv',
'tSukfUOpjhlJywrBNLqdsCMQgocKem',
'uGkrsXedQwgthPBnUROKWxMpbAzIHS',
'FpYhUogyqsjObDHEWlrtmzaTdAIVZR',
'AYqXWkvTIxfgbELnrHOKSBlsGhtCeD',
'XtedjgBGKaRomAYyNrFiCDhIJMfvHq',
'TkWvbdBIUjZDLVCHeQoAityOSGsEXR',
'aqnJjkGwiMxXVIsLTRZHehtyrNzBAP',
'LfDaOWNsnrqpvwPmTtFhCUbolVXQHg',
'lkyKPLYCOSHjaRJUVcquhpFAwteQMB',
'ydUCjSHBtbTGeRzlQYpkghawiWnIDc',
'RETsYVatMnbreLWKGJklSjpoxwuNDZ',
'TYbuimCchQPeZnwyRqvsXWNzDxkGfO',
'UFuWYPQXLjevhitInmCGpwocSNZBHb',
'AxSHvdFGKNDVPLnQshTtZkeYaJWmBz',
'IrymtalebGpgFSXHQdBUnLhOfijvVC',
'YsrqKSTILRXkefiGEMpojbUZcPudhQ',
'dRKibPAhLZpmNeUFTIXOEuQwylvtVz',
'nykjRZsErvNmwzTJQMxSIGbOheFdXp',
'SioVERwbDFqmjAYvKxGcBlWUrfkuQZ',
'gWsIvSEyUJBTqQXcAzdPfjmwauFiYV',
'ChNtkDSpTiVczmWyIvMLlBoKseRauA',
'kWPvXfIAcaBSbtsGudUYCjzhngQxEK',
'eKvtkCQRFBopWZbExOymwLuSHqfDaM',
'yvbXJsnWrfIKopLVUZhHPRQecTENFO',
'FavzcmjlgdCLrXqPAoENufDOUsbxZi',
'uhoHUlYSwvaKePkItTxdnOcMLAJCQj',
'AgahKNdRQzGkoSVfveJlFBbPjITDXW',
'CqTcdBKOmfkJYirnEPgvzNLahHjGSo',
'zRbcOUKvJDwlnEVxZGCpsrBjeLIFgA',
'rwVfyiYAblhFjZzTLoCsDeEBSdtUgI',
'rhKMwkFeOcDAVqGmTbNsHvySQdjYgu',
'CREkoYXmNpxAwfVjiQBZlhbOtIDvdK',
'cqPDHwTtbIioukmOeEKvgMYUjVhXax',
'BHSeksixTLDynKrNVXYRjdvUtzCbMm',
'bFluPatUjeWMHZIqiCRhgzKvGNBpcQ',
'FAXQjLiwmgMDxBrEbndtkVOyfYvCSU',
'dKqEVOMPnTosSxXmYCzAHhRpkZatWi',
'utIJqUlPcbvCyVBHOzWjRaTsodGFXm',
'aMQWhXHAPJizDqKZBtpkSlGrICFmTy',
'GnVQLKTAEwSZYgydmalIWfNFCtOXhM',
'mdFiHBgVzbasuSKhnrXYUfNteIMxEQ',
'AXxOSpUNvZRsHIlcagGiuWLJetQrBk',
'AxXKinPQzlEOYorJsNqCjaWHetSMVU',
'mYiyNrULfWPFEOSXQDhTIklHRMjBgc',
'ryBWhtdcgnMPeDxKAfwlvuVoqSziCO',
'MCPIJpXEDkGecLyztvROmUbWTwsKdj',
'uHJwEQpZvmRNSlgxGFTWehOjnCBsVL',
'CpJSunIUXkfEZlHNtFdgysLqKmYMRD',
'GHiqdQDZoKjzmYJFswNLVUMEPIxhfS',
'oieUGusckOdXfrWhZQJVapDlKBNYCS',
'RcXPVqvguUFbYEzBQslHAIWimLMxdC',
'RdijZMuCAEewHmTnpsUJQYDKxfczOF',
'VNKAzafeZIgHmPobsiYGdqScEprvOB',
'HCJYjaxwQrhzoFcmBIiGkXutDveWNK',
'tWofNXTerKHiLFaOxPkCjmhYlugqME',
'XANqUYworIFbOmGiWxRKMhslDjctBp',
'pxPaWunDyBsqAoGKVHtmvMjwJfdXNl',
'vzdTRVfZGpwKXuabonDxIiLcFEyQqP',
'JwSXpNatDuWiLhfIPEeTKrnBAjVmOH',
'JTYhHRnpmWMuQVwxcbOCNXdazEIBfo',
'mBFNeJZqfKMXiubgGavPREoHpOLdjT',
'EgNxzSHOGPlCXncthToVwaybMpjJZD',
'eNBFDMITQmdHUPwpnRVlyxcJSKAisa',
'EUBgTYFplKSGLvkXVuwoHrbhyNDJne',
'WHNxKahsInmVqGFUAtoePdROczpYQj',
'sSPfjkyFNzbYXAcgoeupMiVKtRWLZH',
'kLzacIjNrFRyuEwvQKgVlMftiWsCxh',
'CoxvVPcYFbLAnBqHZIOzSkhfgTdJEt',
'DlZJQXqeGPuNzyvYTxmpwKsfagiMBo',
'jXfbSJmhlRrVAHYzCMkvGLtFTecgwP',
'uoeJpjckvBfFEWaAXSIKCbwUtzVdNx',
'uosDITKclRkSzZdNMUWHXgynvwhPmV',
'hoydNtmGHTaepDguArLnVsJkbYRwcK',
'DVhdFfnTmwNlEYgyrAvqacCsxMPuZU',
'KwMCURaEOpitDmFnHBgXscqZyYlveG',
'rVWHQnlYtUFLvEsgGOxdNKzoJjIucT',
'lTDiYwjUKbyvmxcEohPLurIRNHAsBp',
'HbJYzLfPSWZFKnUsRjGkmXyBirQVMq',
'iULWlyKHQoYvkGpMFzEZPtXngeCcDV',
'OIUqtkWCFplJNVfLyaxThcSrQKjRGA',
'EZaLbvuKOxHfJelPnrpkDYiVWFqNXh',
'NUzFquLIOjsGgDhVopmRWltBrTKeYC',
'uEazOqKrvhoUcRCNmDGdkpnHtLMlyT',
'MzgsaniSARbkdGhtyflwTQcOvXBYFC',
'kaEPLDewsAMgFRftbiISKyVTGlHqXr',
'USKwjyruaztQdBTMZomkqVNGJWRLnX',
'TzHMqaKJFIZxugrSnmdPjXRQslwLvp',
'LzfuxAiapomWBwDteGHMYTJQsXNIKF',
'EOstFSMhfyUTvKgucGjwkJpoQnXBZV',
'InoZPjwXxqbTcuyVtGWpgYOlAzDHdR',
'ryFCctxGQlkTXnvPeWJdhofMUOHZAV',
'aqcZUVMGmiWswPAytkNeYnOJvlIbXH',
'wsCYOGWoqhjEAVLuxXQBdJnmlFiHpN',
'fRLZBOxEHkiCqgdKcmJYsnDQUvrhyz',
'qXoOupeaPwvhMcCDRrilUQAnNzEJTF',
'IejVfrLRdHBcmwXiCMFhqPoWukgvYn',
'QwCGOHkLEhfAbpJqaKvZIlVzSoFrTD',
'UmbeNAQkOYBXCFWzSyiHoPqhZdEuxs',
'mpaObxFqJonvGIQKyClRNtTwufShdj',
'XGNigBUCqJpxfyLYekmdPVsFQRnAhl',
'CrqLwzxYjoIbDmTMXeHBJlhSvfuRiV',
'XECtzRqApaeUNcGuvifSJnMmbVTYjw',
'VKFmtQcUnjRxvepsCySMlXiPHZGdLo',
'VBfxndOUEHmRbAkJsgtFIcDeZYNoaw',
'epLOUzSAHKWrucxGJbFVBdniTtDZNy',
'FbjrUTOoyDZXiEMIKSdVRBGwnvqxtc',
'gfyMxbnwrkQmcTJGKDEPzSWYdlRiqs',
'ueafMRNDyoWjSvPqXhwrgIUBZVAsOt',
'qCDGHToJdIBFYNXzsVWUbmZlMiepfv',
'yjaFWTkVumMNdGSiLwRIDHQcKOXvqB',
'SDipcGdoXVuRjyAzOCQgwavKFneltx',
'FLxVojwrNndGfPKkBvaTJuAYiXhZIq',
'tAnOQHCxcbsrugqXlomYivkhdNjRaG',
'ZypItMxEaJoPeOLVNlFXHYSAsbjRTw',
'WpEmeyTrKionFtYDZQSfcuPgXOMGhH',
'MXgxiETHebYULtVACmkpnsFuBKGadh',
'CjbPRZoaDHtpMfVmQqEWcYihkBnSNu',
'iZRYLIPBWXMEKUmNfHAzOuxqQagndt',
'dHSkNwVzXhqisbJnABKfCDMEPOIyjm',
'AfKnimpGxHcjXTUabvQegEFhYOkWqR',
'gtiUuqmsdYSPXBaREfMAJDxCnHhbzG',
'AxmrnuIVaZlXbGMweOSHWyRcNzLdiE',
'OuHeDFrbIEjGvQUWnizkALRJcmgyXw',
'TbhmMlaovUdZrLDjOFGSKfVHuPcIws',
'DwvELheBTsgJCypMqRXVtNHSGcdkWu',
'jSHDtVxXmzdCIrlvBMRNchfaTkGEKW',
'ndAhgUHMbYeTDaIrvzJuKpwXNjqmFL',
'soFfQMeXPtGhNcxqWbyrlDLmuaKgUZ',
'pHjFKPxtGRqsOimedCBlwYMASQDhbk',
'KLIOnJBiTcuVgQNtqxrbSmDUARaZly',
'zrNjlboiXuPnUSDZRxvYkfwBtWHEhC',
'jDsxhNTCdXvpBefYMlgiqLkIFQPEZz',
'ESeVyNTflsICkLgFmUMiJBKZhvHprR',
'sENPztCbxBGvdaMqDXWTZuenQHilkY',
'nXquSwtyBeJmNVHbPiYLoTRFdGExKf',
'SrdTkGMAIQPJplvDmuZEeafBKzqoHY',
'hikYcOVBsfzIgGymuMADaQtpWrwjHl',
'RDpIAMxzriuPlZSjavCYWkgVOFLnbN',
'XuoLZksaFQRHUlTWcqKOSrECVzvmnY',
'DUyksALgarFitbMzOYfwdcJTRqSXBZ',
'nedFMSvpZgiYJRIwOmbzKAGaEjsWfh',
'ptLvxraYyMjERVKHswkSJiXcFzmOuZ',
'ozJqmnbQEWYdTARUxrSilFZehfBuON',
'PLvoAFlWbsBHKTNyaeGzSwEcpZtigV',
'CRkvAZDnjhLmeHVGbQIdaOrKiPBMxS',
'AtRIuBNLyFjmUPzOHWlaebdVZiDqsQ',
'hyZEDLXzAYduJvsMtPjcqkmWpglUVB',
'UhgsOLNmuZDtfKeTMwFpPlkYjyvVHc',
'xmYEPBkcjeVSazAJMORbCDLyrtXsgd',
'BsfElynRoFtQjuYDgLkSaZIvdpMVmC',
'GhpNAViRroKBDWCtjcJIeXTudOnbxz',
'RGdrOvKncIXjDxzEZeqgswVhyUHWoF',
'lDyWOhMexuTANYaHBfgPQpKsIrRJzw',
'tpjLmKqgXMwZaAhBUlvFPxCzbocryD',
'yVHgXBEpFQSdecTbKOkLunfAzGYtxo',
]

template = '''
#include <stdio.h>
#include <stdlib.h>

char *alpha = "{alphabet}";
void auth() {{
    int password[40] = {{
        {passw[0]},
        {passw[1]},
        {passw[2]},
        {passw[3]},
        {passw[4]},
        {passw[5]},
        {passw[6]},
        {passw[7]},
        {passw[8]},
        {passw[9]},
        {passw[10]},
        {passw[11]},
        {passw[12]},
        {passw[13]},
        {passw[14]},
        {passw[15]},
        {passw[16]},
        {passw[17]},
        {passw[18]},
        {passw[19]},
        {passw[20]},
        {passw[21]},
        {passw[22]},
        {passw[23]},
        {passw[24]},
        {passw[25]},
        {passw[26]},
        {passw[27]},
        {passw[28]},
        {passw[29]},
        {passw[30]},
        {passw[31]},
        {passw[32]},
        {passw[33]},
        {passw[34]},
        {passw[35]},
        {passw[36]},
        {passw[37]},
        {passw[38]},
        {passw[39]},
    }};
    char input[41];
    int len = {le};
    fgets(input, len+1, stdin);
    for (int i=0; i<len; i++) {{
        if (input[i] != alpha[password[i]]) {{
            puts("Wrong pass");
            exit(1);
        }}
    }}
    printf("good job");
}}

int main() {{
    auth();
}}
'''

import os
import random
import time
import tempfile
import base64

random.seed(time.time())

def compile(filename):
    outputfile = filename + '.out'
    os.system('gcc {0} -o {1} -s'.format(filename+'.c', outputfile))
    return outputfile

def write_to_file(filename, source):
    open(filename + '.c', 'w').write(source)


def generate_rand_source():
    le = random.randint(20, 30)
    indices = list(range(0, le))
    random.shuffle(indices)
    alphabet = random.choice(alphabets)
    password = ''.join(alphabet[i] for i in indices)

    indices = (indices + [0]*40)[:40]
    source = template.format(
        alphabet = alphabet,
        le=le,
        passw = indices,
    )
    return (source, password)

import sys
def error(msg):
    print(msg)
    sys.exit(1)

t = tempfile.mktemp()
for i in range(100):
    source, passw = generate_rand_source()
    write_to_file(t, source)

    out = compile(t)
    print(base64.b64encode(open(out).read()))
    inp = raw_input()
    if inp != passw:
        error('wrong password, lol')

print(open('flag.txt').read())
