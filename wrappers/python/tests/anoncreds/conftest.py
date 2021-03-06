import json

import pytest

from indy import anoncreds
from tests.conftest import path_home as x_path_home, pool_name as x_pool_name, wallet_name as x_wallet_name, \
    wallet_type as x_wallet_type, wallet_runtime_config as x_wallet_runtime_config, \
    xwallet_cleanup as x_xwallet_cleanup, wallet_handle_cleanup as x_wallet_handle_cleanup, \
    wallet_handle as x_wallet_handle, \
    xwallet as x_xwallet


@pytest.fixture(scope="module")
def path_home():
    # noinspection PyTypeChecker
    for i in x_path_home():
        yield i


@pytest.fixture(scope="module")
def pool_name():
    return x_pool_name()


@pytest.fixture(scope="module")
def wallet_name():
    return x_wallet_name()


@pytest.fixture(scope="module")
def wallet_type():
    return x_wallet_type()


@pytest.fixture(scope="module")
def wallet_runtime_config():
    return x_wallet_runtime_config()


@pytest.fixture(scope="module")
def xwallet_cleanup():
    return x_xwallet_cleanup()


# noinspection PyUnusedLocal
@pytest.fixture(scope="module")
def xwallet(event_loop, pool_name, wallet_name, wallet_type, xwallet_cleanup, path_home):
    xwallet_gen = x_xwallet(event_loop, pool_name, wallet_name, wallet_type, xwallet_cleanup, path_home)
    yield next(xwallet_gen)
    next(xwallet_gen)


@pytest.fixture(scope="module")
def wallet_handle_cleanup():
    return x_wallet_handle_cleanup()


@pytest.fixture(scope="module")
def wallet_handle(event_loop, wallet_name, xwallet, wallet_runtime_config, wallet_handle_cleanup):
    wallet_handle_gen = x_wallet_handle(event_loop, wallet_name, xwallet, wallet_runtime_config, wallet_handle_cleanup)
    yield next(wallet_handle_gen)
    next(wallet_handle_gen)


@pytest.fixture(scope="module")
def issuer_did():
    return "NcYxiDXkpYi6ov5FcYDi1e"


@pytest.fixture(scope="module")
def issuer_did_2():
    return "NcYxiDXkpYi6ov5FcYDi1e3"


@pytest.fixture(scope="module")
def prover_did():
    return "CnEDk9HrMnmiHXEV1WFgbVCRteYnPqsJwrTdcZaNhFVW"


@pytest.fixture(scope="module")
def schema_seq_no():
    return 1


@pytest.fixture(scope="module")
def schema_seq_no_2():
    return 2


@pytest.fixture(scope="module")
def master_secret_name():
    return "common_master_secret_name"


@pytest.fixture(scope="module")
def master_secret_name_1():
    return "common_master_secret_name_1"


@pytest.fixture(scope="module")
def master_secret_name_2():
    return "common_master_secret_name_2"


@pytest.fixture(scope="module")
def schema_key(issuer_did):
    return {
        'name': 'gvt',
        'version': '1.0',
        'did': issuer_did
    }


@pytest.fixture(scope="module")
def schema_key_json(schema_key):
    return json.dumps(schema_key)


@pytest.fixture(scope="module")
def xyz_schema_key(issuer_did):
    return {
        'name': 'xyz',
        'version': '1.0',
        'did': issuer_did
    }


@pytest.fixture(scope="module")
def schema_key_json(schema_key):
    return json.dumps(schema_key)


def claim_offer(issuer_did, schema_key):
    return {"issuer_did": issuer_did, "schema_key": schema_key}


@pytest.fixture(scope="module")
def claim_offer_issuer_1_schema_1(issuer_did, schema_key):
    return claim_offer(issuer_did, schema_key)


@pytest.fixture(scope="module")
def claim_offer_issuer_1_schema_1_json(claim_offer_issuer_1_schema_1):
    return json.dumps(claim_offer_issuer_1_schema_1)


@pytest.fixture(scope="module")
def claim_offer_issuer_1_schema_2(issuer_did, xyz_schema_key):
    return claim_offer(issuer_did, xyz_schema_key)


@pytest.fixture(scope="module")
def claim_offer_issuer_1_schema_2_json(claim_offer_issuer_1_schema_2):
    return json.dumps(claim_offer_issuer_1_schema_2)


@pytest.fixture(scope="module")
def claim_offer_issuer_2_schema_1(issuer_did_2, schema_key):
    return claim_offer(issuer_did_2, schema_key)


@pytest.fixture(scope="module")
def claim_offer_issuer_2_schema_1_json(claim_offer_issuer_2_schema_1):
    return json.dumps(claim_offer_issuer_2_schema_1)


@pytest.fixture(scope="module")
def claim_offer_prover_2(prover_did, xyz_schema_key):
    return claim_offer(prover_did, xyz_schema_key)


@pytest.fixture(scope="module")
def claim_offer_prover_2_json(claim_offer_prover_2):
    return json.dumps(claim_offer_prover_2)


@pytest.fixture(scope="module")
def gvt_schema(schema_seq_no: int, issuer_did: str):
    return {
        "seqNo": schema_seq_no,
        "dest": issuer_did,
        "data": {
            "name": "gvt",
            "version": "1.0",
            "attr_names": ["age", "sex", "height", "name"]
        }
    }


@pytest.fixture(scope="module")
def xyz_schema(schema_seq_no: int, issuer_did: str):
    return {
        "seqNo": 2,
        "dest": issuer_did,
        "data": {
            "name": "xyz",
            "version": "1.0",
            "attr_names": ["period", "status"]
        }
    }


@pytest.fixture(scope="module")
def gvt_schema_json(gvt_schema):
    return json.dumps(gvt_schema)


@pytest.fixture(scope="module")
def xyz_schema_json(xyz_schema):
    return json.dumps(xyz_schema)


@pytest.fixture(scope="module")
def gvt_claim():
    return {
        "sex": ["male", "5944657099558967239210949258394887428692050081607692519917050011144233115103"],
        "name": ["Alex", "1139481716457488690172217916278103335"],
        "height": ["175", "175"],
        "age": ["28", "28"]
    }


@pytest.fixture(scope="module")
def gvt_claim_json(gvt_claim):
    return json.dumps(gvt_claim)


@pytest.fixture(scope="module")
def gvt_claim_2():
    return {
        "sex": ["male", "2142657394558967239210949258394838228692050081607692519917028371144233115103"],
        "name": ["Alexander", "21332817548165488690172217217278169335"],
        "height": ["170", "170"],
        "age": ["28", "28"]
    }


@pytest.fixture(scope="module")
def gvt_2_claim_json(gvt_claim):
    return json.dumps(gvt_claim)


@pytest.fixture(scope="module")
def xyz_claim():
    return {
        "status": ["partial", "51792877103171595686471452153480627530895"],
        "period": ["8", "8"]
    }


@pytest.fixture(scope="module")
def xyz_claim_json(xyz_claim):
    return json.dumps(xyz_claim)


@pytest.fixture(scope="module")
def claim_req(issuer_did, schema_key):
    return {"blinded_ms": {"u": "541727375645293327107242131390489410830131768916446771173223218236303087346206273292"
                                "275918450941006362568297619591573147842939390451766213271549909084590728218268187187"
                                "396963232997879281735355290245565403237095788507069932942349664408266908992668726827"
                                "902285139739992123705745482398771085112836294238073386324354310973398756650754537851"
                                "417229890983878959703959824327090115058645337274155525667150696753462207525844495604"
                                "072614465677317118141888367033373659867254296561952756168465435357073642154989807508"
                                "60746440672050640048215761507774996460985293327604627646056062013419674090094698841"
                                "792968543317468164175921100038",
                           "ur": None},
            "prover_did": "CnEDk9HrMnmiHXEV1WFgbVCRteYnPqsJwrTdcZaNhFVW",
            "issuer_did": issuer_did, "schema_key": schema_key}


@pytest.fixture(scope="module")
def claim_req_json(claim_req):
    return json.dumps(claim_req)


@pytest.fixture(scope="module")
def predicate_value():
    return 18


@pytest.fixture(scope="module")
def proof_req(predicate_value, schema_key):
    return {
        "nonce": "123432421212",
        "name": "proof_req_1",
        "version": "0.1",
        "requested_attrs": {
            "attr1_referent":
                {
                    "name": "name",
                    "restrictions": [{"schema_key": schema_key}]
                }
        },
        "requested_predicates": {
            "predicate1_referent": {
                "attr_name": "age",
                "p_type": ">=",
                "value": predicate_value
            }
        }
    }


@pytest.fixture(scope="module")
def proof_req_json(proof_req):
    return json.dumps(proof_req)


@pytest.fixture(scope="module")
def claim_def(issuer_did):
    return {
        "ref": 1,
        "signature_type": "CL",
        "origin": issuer_did,
        "data": {
            "primary": {
                "n": "94759924268422840873493186881483285628376767714620627055233230078254863658476446487556117977593248501523199451418346650764648601684276437772084327637083000213497377603495837360299641742248892290843802071224822481683143989223918276185323177379400413928352871249494885563503003839960930062341074783742062464846448855510814252519824733234277681749977392772900212293652238651538092092030867161752390937372967233462027620699196724949212432236376627703446877808405786247217818975482797381180714523093913559060716447170497587855871901716892114835713057965087473682457896508094049813280368069805661739141591558517233009123957",
                "s": "3589207374161609293256840431433442367968556468254553005135697551692970564853243905310862234226531556373974144223993822323573625466428920716249949819187529684239371465431718456502388533731367046146704547241076626874082510133130124364613881638153345624380195335138152993132904167470515345775215584510356780117368593105284564368954871044494967246738070895990267205643985529060025311535539534155086912661927003271053443110788963970349858709526217650537936123121324492871282397691771309596632805099306241616501610166028401599243350835158479028294769235556557248339060399322556412171888114265194198405765574333538019124846",
                "rms": "57150374376895616256492932008792437185713712934712117819417607831438470701645904776986426606717466732609284990796923331049549544903261623636958698296956103821068569714644825742048584174696465882627177060166162341112552851798863535031243458188976013190131935905789786836375734914391914349188643340535242562896244661798678234667651641013894284156416773868299435641426810968290584996112925365638881750944407842890875840705650290814965768221299488400872767679122749231050406680432079499973527780212310700022178178822528199576164498116369689770884051691678056831493476045361227274839673581033532995523269047577973637307053",
                "r": {
                    "age": "94304485801056920773231824603827244147437820123357994068540328541540143488826838939836897544389872126768239056314698953816072289663428273075648246498659039419931054256171488371404693243192741923382499918184822032756852725234903892700640856294525441486319095181804549558538523888770076173572615957495813339649470619615099181648313548341951673407624414494737018574238782648822189142664108450534642272145962844003886059737965854042074083374478426875684184904488545593139633653407062308621502392373426120986761417580127895634822264744063122368296502161439648408926687989964483291459079738447940651025900007635890755686910",
                    "sex": "29253365609829921413347591854991689007250272038394995372767401325848195298844802462252851926995846503104090589196060683329875231216529049681648909174047403783834364995363938741001507091534282239210301727771803410513303526378812888571225762557471133950393342500638551458868147905023198508660460641434022020257614450354085808398293279060446966692082427506909617283562394303716193372887306176319841941848888379308208426966697446699225783646634631703732019477632822374479322570142967559738439193417309205283438893083349863592921249218168590490390313109776446516881569691499831380592661740653935515397472059631417493981532",
                    "name": "25134437486609445980011967476486104706321061312022352268621323694861467756181853100693555519614894168921947814126694858839278103549577703105305116890325322098078409416441750313062396467567140699008203113519528887729951138845002409659317083029073793314514377377412805387401717457417895322600145580639449003584446356048213839274172751441145076183734269045919984853749007476629365146654240675320041155618450449041510280560040162429566008590065069477149918088087715269037925211599101597422023202484497946662159070023999719865939258557778022770035320019440597702090334486792710436579355608406897769514395306079855023848170",
                    "height": "59326960517737425423547279838932030505937927873589489863081026714907925093402287263487670945897247474465655528290016645774365383046524346223348261262488616342337864633104758662753452450299389775751012589698563659277683974188553993694220606310980581680471280640591973543996299789038056921309016983827578247477799948667666717056420270448516049047961099547588510086600581628091290215485826514170097211360599793229701811672966818089371089216189744274422526431130783428589346341196561742409198605034972210917502326180305735092988639850309253190875578501020679137562856724998821945605494355779034135306337094344532980411836"
                },
                "rctxt": "9641986614889199796257508700106896585587271615330980339636468819377346498767697681332046156705231986464570206666984343024200482683981302064613556104594051003956610353281701880542337665385482309134369756144345334575765116656633321636736946947493150642615481313285221467998414924865943067790561494301461899025374692884841352282256044388512875752628313052128404892424405230961678931620525106856624692942373538946467902799339061714326383378018581568876147181355325663707572429090278505823900491548970098691127791086305310899642155499128171811034581730190877600697624903963241473287185133286356124371104261592694271730029",
                "z": "77594127026421654059198621152153180600664927707984020918609426112642522289621323453889995053400171879296098965678384769043918218957929606187082395048777546641833348694470081024386996548890150355901703252426977094536933434556202865213941384425538749866521536494046548509344678288447175898173634381514948562261015286492185924659638474376885655055568341574638453213864956407243206035973349529545863886325462867413885904072942842465859476940638839087894582648849969332663627779378998245133055807038199937421971988505911494931665143822588532097754480882750243126847177560978100527491344463525107644125030963904001009159559"
            },
            "revocation": None
        }
    }


@pytest.fixture(scope="module")
def claim_def_json(claim_def):
    return json.dumps(claim_def)


@pytest.fixture(scope="module")
async def prepopulated_wallet(wallet_handle, gvt_schema_json, xyz_schema_json, gvt_claim_json, gvt_2_claim_json,
                              xyz_claim_json, issuer_did, issuer_did_2, master_secret_name,
                              claim_offer_issuer_1_schema_1_json, claim_offer_issuer_1_schema_2_json,
                              claim_offer_issuer_2_schema_1_json, prover_did):
    await anoncreds.prover_store_claim_offer(wallet_handle, claim_offer_issuer_1_schema_1_json)
    await anoncreds.prover_store_claim_offer(wallet_handle, claim_offer_issuer_1_schema_2_json)
    await anoncreds.prover_store_claim_offer(wallet_handle, claim_offer_issuer_2_schema_1_json)

    await anoncreds.prover_create_master_secret(wallet_handle, master_secret_name)

    # Create GVT Claim by Issuer1
    claim_def_json = await anoncreds.issuer_create_and_store_claim_def(
        wallet_handle, issuer_did, gvt_schema_json, None, False)

    claim_req = await anoncreds.prover_create_and_store_claim_req(
        wallet_handle, prover_did, claim_offer_issuer_1_schema_1_json, claim_def_json, master_secret_name)

    (_, claim_json) = await anoncreds.issuer_create_claim(wallet_handle, claim_req, gvt_claim_json, -1)

    await anoncreds.prover_store_claim(wallet_handle, claim_json, None)

    # Create XYZ Claim by Issuer1
    claim_def_json_2 = await anoncreds.issuer_create_and_store_claim_def(
        wallet_handle, issuer_did, xyz_schema_json, None, False)

    claim_req = await anoncreds.prover_create_and_store_claim_req(
        wallet_handle, prover_did, claim_offer_issuer_1_schema_2_json, claim_def_json_2, master_secret_name)

    (_, claim_json) = await anoncreds.issuer_create_claim(wallet_handle, claim_req, xyz_claim_json, -1)

    await anoncreds.prover_store_claim(wallet_handle, claim_json, None)

    # Create GVT Claim by Issuer2
    claim_def_json_3 = await anoncreds.issuer_create_and_store_claim_def(
        wallet_handle, issuer_did_2, gvt_schema_json, None, False)

    claim_req = await anoncreds.prover_create_and_store_claim_req(
        wallet_handle, prover_did, claim_offer_issuer_2_schema_1_json, claim_def_json_3, master_secret_name)

    (_, claim_json) = await anoncreds.issuer_create_claim(wallet_handle, claim_req, gvt_2_claim_json, -1)

    await anoncreds.prover_store_claim(wallet_handle, claim_json, None)

    return claim_def_json,
