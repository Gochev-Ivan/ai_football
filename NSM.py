from constants import *
import numpy as np
import cmath as cm

gl_prom_sm = 1
gl_proslo_y = post_screen_top
gl_na_golu = 0
topka_pr_x = center[0]
topka_pr_y = center[1]
vlopte = 0
golman_pr_x = center[0]
golman_pr_y = center[1]
vgolman = 0
bloker_pr_x = center[0]
bloker_pr_y = center[1]
vbloker = 0
dribler_pr_x = center[0]
dribler_pr_y = center[1]
vdribler = 0
pravac = 1

golman_na_go = 1


def zona(our_side, x, y):
    ytop = 50 + int(resolution[1] / 5)
    duzina = resolution[0] - 100
    x -= 50
    y -= ytop

    if our_side == 'right':
        x = duzina - x

    post_gore = post_screen_top - ytop
    post_dole = post_screen_bottom - ytop

    if (x < 0.25 * duzina and x > 0.08 * duzina) or (x < 0.08 * duzina and y > post_gore and y < post_dole):
        return 0
    elif x > 0.45 * duzina:
        return 2
    else:
        return 1


def init(our_team, ball):
    global vlopte
    global pravac
    global vbloker
    global vdribler
    global vgolman
    vlopte, pravac = brzina_lopte(ball)
    vbloker = rastojanje(bloker_pr_x, bloker_pr_y, our_team[2]['x'], our_team[2]['y']) / dt
    our_team[2]['v'] = vbloker
    vdribler = rastojanje(dribler_pr_x, dribler_pr_y, our_team[1]['x'], our_team[1]['y']) / dt
    our_team[1]['v'] = vdribler
    vgolman = rastojanje(golman_pr_x, golman_pr_y, our_team[0]['x'], our_team[0]['y']) / dt
    our_team[0]['v'] = vgolman


def brzina_lopte(ball):
    global topka_pr_y
    global topka_pr_x
    pravac = 1
    d = np.sqrt((ball['x'] - topka_pr_x) ** 2 + (ball['y'] - topka_pr_y) ** 2)
    if ball['x'] < topka_pr_x:
        pravac = -1
    topka_pr_x = ball['x']
    topka_pr_y = ball['y']
    v_l = d / dt
    return v_l, pravac


def po_y_osi(golman, y_u_golu, ogranicenje):
    global gl_prom_sm
    global gl_proslo_y

    if ogranicenje:
        if y_u_golu < post_screen_top:
            y_u_golu = post_screen_top
        if y_u_golu > post_screen_bottom:
            y_u_golu = post_screen_bottom

    if gl_prom_sm == 0:
        sila = golman['mass'] * golman['a_max'] + 1
    else:
        sila = -(golman['mass'] * golman['a_max'] + 1)
    if golman['y'] < y_u_golu:
        ugao = np.pi / 2
    else:
        ugao = -np.pi / 2

    if ugao != golman['alpha']:
        gl_prom_sm = gl_prom_sm + 1

    if gl_proslo_y != y_u_golu:
        gl_prom_sm = 0
        gl_proslo_y = y_u_golu
    golman['force'] = sila
    golman['alpha'] = ugao
    golman['shot_request'] = False
    golman['shot_power'] = 0


def da_li_je_sutnuta(ball):
    global vlopte
    prag = 350  # promeniti
    return vlopte >= prag


def min_vreme_do_lopte(player, ball):
    global vlopte
    beta = ball['alpha']
    xl = ball['x']
    yl = ball['y']
    xi = player['x']
    yi = player['y']
    if xi == xl:
        return 1000000
    k = (yi - yl) / (xi - xl)
    sinus = vlopte / player['v_max'] * (k * np.cos(beta) - np.sin(beta)) / np.sqrt(k ** 2 + 1)
    fi = cm.phase(complex(xl - xi, yl - yi))
    if sinus > 1 or sinus < -1:
        return 1000000
    alfa1 = fi - np.arcsin(sinus)
    alfa2 = fi - np.pi + np.arcsin(sinus)
    ts1 = (yi - yl) / (vlopte * np.sin(beta) - player['v_max'] * np.sin(alfa1))
    ts2 = (yi - yl) / (vlopte * np.sin(beta) - player['v_max'] * np.sin(alfa2))
    if ts1 * ts2 > 0:
        return 1000000
    elif ts1 > 0:
        return ts1
    else:
        return ts2


def blizi_od_svih(golman, their_team, ball):
    tg = 1.1 * min_vreme_do_lopte(golman, ball)
    t0 = min_vreme_do_lopte(their_team[0], ball)
    t1 = min_vreme_do_lopte(their_team[1], ball)
    t2 = min_vreme_do_lopte(their_team[2], ball)
    return (tg < t0 and tg < t1 and tg < t2)


def pozicioniraj(ball, player, xzeljeno, yzeljeno, nasa_strana):
    r = player['radius'] + ball['radius'] + 3
    if xzeljeno == ball['x']:
        imenilac = 0.001
    else:
        imenilac = xzeljeno - ball['x']
    k = (yzeljeno - ball['y']) / imenilac
    x1 = ball['x'] - r * nasa_strana / (np.sqrt(1 + k * k))
    y1 = ball['y'] - k * (ball['x'] - x1)
    player['shot_request'] = False
    player['shot_power'] = 0
    trci(player, x1, y1)


def nadji_putanju_za_ispucavanje(ball, golman, their_team, our_side):
    ytop = 50 + int(resolution[1] / 5)
    ybot = resolution[1] - 50

    nasx = golman['x']
    niz = []
    i = 0
    n = 0
    while i < 3:
        if (their_team[i]['x'] > nasx):
            niz.append(their_team[i])
            n = n + 1
        i = i + 1
    i = 0
    if n == 0:
        if our_side == 'left':
            xzeljeno = post_screen_right
            yzeljeno = (post_screen_top + post_screen_bottom) / 2
        else:
            xzeljeno = post_screen_left
            yzeljeno = (post_screen_top + post_screen_bottom) / 2
        return xzeljeno, yzeljeno

    while i < n - 1:
        j = i + 1
        while j < n:
            if niz[i]['y'] > niz[j]['y']:
                p = niz[i]
                niz[i] = niz[j]
                niz[j] = p
            j = j + 1
        i = i + 1

    tackex = []
    tackex.append(niz[0]['x'])
    tackey = []
    tackey.append(ytop)

    i = 0
    j = 0

    while j < n:
        a1, a2, a3, a4 = tangenta(niz[j]['x'], niz[j]['y'], ball['x'], ball['y'], niz[j]['radius'])
        tackex.append(a1)
        tackex.append(a3)
        tackey.append(a2)
        tackey.append(a4)

        i = i + 2
        j = j + 1

    tackex.append(niz[n - 1]['x'])
    tackey.append(ybot)

    brTacaka = i

    i = 0
    j = 0

    # n = len(tackey)
    # while i < n - 1:
    #     j = i + 1
    #     while j < n:
    #         if tackey[i] > tackey[j]:
    #             p = tackex[i]
    #             tackex[i] = tackex[j]
    #             tackex[j] = p
    #             p = tackey[i]
    #             tackey[i] = tackey[j]
    #             tackey[j] = p
    #         j += 1
    #     i += 1

    fi = []

    i = 0
    while i < brTacaka:
        fi.append(kosinusna(ball['x'], ball['y'], tackex[i], tackey[i], tackex[i + 1], tackey[i + 1]))
        i += 2
    fi[0] *= 2
    fi[int(brTacaka / 2) - 1] *= 2

    i = 1
    max = 0
    while i < brTacaka / 2:
        if fi[max] < fi[i]:
            max = i
        i += 1

    if max == 0:
        xzeljeno = tackex[0]
        yzeljeno = ytop
    elif max == brTacaka / 2 - 1:
        xzeljeno = tackex[brTacaka - 1]
        yzeljeno = ybot
    else:
        xzeljeno = (tackex[2 * max] + tackex[2 * max + 1]) / 2
        yzeljeno = (tackey[2 * max] + tackey[2 * max + 1]) / 2

    return xzeljeno, yzeljeno


def istrci_i_ispucaj(ball, player, their_team, our_side):
    if our_side == 'left':
        nasa_strana1 = 1
    else:
        nasa_strana1 = -1
    if rastojanje(ball['x'], ball['y'], player['x'], player['y']) > player['radius'] + ball['radius'] + 5:
        xzeljeno, yzeljeno = nadji_putanju_za_ispucavanje(ball, player, their_team, our_side)
        pozicioniraj(ball, player, xzeljeno, yzeljeno, nasa_strana1)
    else:
        player['shot_power'] = 100000
        player['shot_request'] = True
        trci(player, ball['x'], ball['y'])


def panicno_istrci(player, ball, our_side):
    if our_side == 'left':
        nasa_strana = -1
    else:
        nasa_strana = 1

    player['shot_power'] = 100000
    player['shot_request'] = True
    trci(player, ball['x'] + (ball['radius'] + player['radius']) * 0.9 * nasa_strana, ball['y'])


def gde_ce_uci(golman, ball, our_side, xkoord):
    alfa = ball['alpha']
    ytop = 50 + int(resolution[1] / 5)
    ybot = resolution[1] - 50
    if (alfa < np.pi / 2 * 1.03 and alfa > np.pi / 2 * 0.97) or (alfa > -np.pi / 2 * 1.03 and alfa < -np.pi / 2 * 0.97):
        return ball['y']
    k = np.tan(alfa)

    if xkoord == -1:
        if our_side == 'left':
            xg = post_screen_left + post_radius + ball['radius'] * 0.8 + golman['radius'] * 2
        else:
            xg = post_screen_right - post_radius - ball['radius'] * 0.8 - golman['radius'] * 2
    else:
        xg = xkoord

    xgola = xg - post_screen_left
    sirina = ybot - ytop

    xlopta = ball['x'] - post_screen_left
    ylopta = ball['y'] - ytop

    y = (k * (xgola - xlopta) + ylopta)
    if y < 0:
        smer = 1
    elif y > sirina:
        smer = -1
    else:
        smer = 0

    broj_puta = 0
    if (smer != 0):
        while (y < 0 or y > sirina):
            y += sirina * smer
            broj_puta += 1
    if broj_puta % 2 == 1:
        y = sirina - y

    y += ytop
    return y


def trci(player, x, y):
    player['alpha'] = cm.phase(complex(x - player['x'], y - player['y']))
    player['force'] = player['mass'] * player['a_max'] + 1


def trci2(player, x, y, vkoef):
    player['alpha'] = cm.phase(complex(x - player['x'], y - player['y']))
    player['force'] = player['mass'] * player['a_max'] * vkoef


def vrati_se_na_gol(player, ball, our_side):
    if player['y'] < post_screen_top:
        y = post_screen_top
    elif player['y'] > post_screen_bottom:
        y = post_screen_bottom
    else:
        y = player['y']
    if our_side == 'left':
        x = post_screen_left + post_radius + ball['radius'] * 0.8 + player['radius']
    else:
        x = post_screen_right - post_radius - ball['radius'] * 0.8 - player['radius']
    trci(player, x, y)
    player['shot_request'] = False
    player['shot_power'] = 0


def tangenta(xc, yc, x1, y1, r):
    alfa = (xc - x1) ** 2 - r ** 2
    beta = (xc - x1) * (yc - y1)
    gama = (yc - y1) ** 2 - r ** 2

    if alfa == 0:
        alfa = 0.01

    a1 = (beta + np.sqrt(beta ** 2 - alfa * gama)) / alfa
    a2 = (beta - np.sqrt(beta ** 2 - alfa * gama)) / alfa

    b1 = y1 - a1 * x1
    b2 = y1 - a2 * x1

    xt1 = (xc - a1 * (b1 - yc)) / (1 + a1 ** 2)
    yt1 = a1 * xt1 + b1

    xt2 = (xc - a2 * (b2 - yc)) / (1 + a2 ** 2)
    yt2 = a2 * xt2 + b2

    if yt2 < yt1:
        return xt2, yt2, xt1, yt1
    else:
        return xt1, yt1, xt2, yt2


def rastojanje(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def kosinusna(xA, yA, xB, yB, xC, yC):
    a = rastojanje(xB, yB, xC, yC)
    b = rastojanje(xA, yA, xC, yC)
    c = rastojanje(xA, yA, xB, yB)

    return np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))


def na_golu(our_side, player, ball):
    if our_side == 'left':
        return player['x'] <= post_screen_left + post_radius + ball['radius'] * 0.8 + player['radius']
    else:
        return player['x'] >= post_screen_right - post_radius - ball['radius'] * 0.8 - player['radius']


golman_radnja = 0  # 0 - vrati se na gol, 1 - prati loptu, 2 - istrci, 3 - panika, 4 - juri ka mestu gde bi lopta usla


def golman_zhmk(our_team, their_team, ball, our_side, half, time_left, our_score, their_score):
    global golman_radnja
    global pravac
    global vlopte
    golman = our_team[0]
    if our_side == 'left':
        nasa_strana = 1
    else:
        nasa_strana = -1

    if not na_golu(our_side, golman, ball) and (nasa_strana * pravac * vlopte) >= 0:  ######################3
        golman_radnja = 0
    elif not na_golu(our_side, golman, ball):
        if ball['x'] * nasa_strana < golman['x'] * nasa_strana:
            # golman_radnja = 0
            print('usaouif')
    else:
        if zona(our_side, ball['x'], ball['y']) == 0 and da_li_je_sutnuta(ball):
            golman_radnja = 4
        elif zona(our_side, ball['x'], ball['y']) == 0 and not da_li_je_sutnuta(ball):
            if blizi_od_svih(golman, their_team, ball):
                golman_radnja = 2
            else:
                golman_radnja = 3
        elif zona(our_side, ball['x'], ball['y']) == 2:
            golman_radnja = 1
        else:
            if not (da_li_je_sutnuta(ball)) and blizi_od_svih(golman, their_team, ball):
                golman_radnja = 2
            elif da_li_je_sutnuta(ball):
                golman_radnja = 4
            else:
                golman_radnja = 1

    if golman_radnja == 0:
        vrati_se_na_gol(golman, ball, our_side)
    if golman_radnja == 1:
        po_y_osi(golman, ball['y'], True)
    if golman_radnja == 2:
        istrci_i_ispucaj(ball, golman, their_team, our_side)
    if golman_radnja == 3:
        panicno_istrci(golman, ball, our_side)
    if golman_radnja == 4:
        y = gde_ce_uci(golman, ball, our_side, -1)
        po_y_osi(golman, y, True)
    return golman['alpha'], golman['force'], golman['shot_request'], golman['shot_power']


# region igraci
##
##
##
##

# def pridji_lopti2(player, ball, xzeljeno, yzeljeno, our_side):
# xlopte = ball['x']
# ylopte = ball['y']
# nasa_strana = 1
# if (our_side=='right'):
#     nasa_strana = -1
# R = player['radius']
# r = ball['radius']
# k = (yzeljeno-ylopte)/(xzeljeno-xlopte)
# fi = cm.phase(complex(1, k))
# xigraca = xlopte-np.cos(fi)*(R+r-1) #xigraca je pozicija gde igrac treba da dodje da bi dalje postupao sa loptom
# yigraca = ylopte-np.sin(fi)*(R+r-1)
# player['shot_request'] = False
# if ylopte==yigraca
# t = -(xlopte-xigraca)/(ylopte-yigraca)
# if t==0:
#     t=0.01
# b = yigraca-t*xigraca
# xciljano = (player['y']-b)/t
# yciljano = player['y']
# if xciljano*nasa_strana<player['x']*nasa_strana:
#     trci(player,xciljano,yciljano)
# else:
#     trci(player,xigraca,yigraca)

def trci_u_krug(player, xc, yc, xz, yz):
    # xc,yc lopte obicno, xz - xzeljeno i yz - zeljeno
    fi0 = cm.phase(complex(player['x'] - xc, player['y'] - yc))
    fik = cm.phase(complex(xz - xc, yz - yc))
    smer = 1  # idemo od x ka y, tj. nadole, matem. poz. smer za njihov xy k.s.
    if (fik > fi0):
        if (fik - fi0 > np.pi):
            smer = -1
    else:
        if ((fik - fi0) > -np.pi):
            smer = -1
    if np.abs(fik - fi0) > 0.15:
        player['alpha'] = smer * np.pi / 2 + fi0
    # if player['v']/player['v_max'] <= 0.6:
    #     player['force'] = 0
    # else:
    #     player['force'] = -player['mass'] * player['a_max']*0.5
    player['force'] = player['mass'] * player['a_max'] + 1


def pridji_lopti(player, ball, xzeljeno, yzeljeno, ukontaktu):
    player['shot_request'] = False
    player['shot_power'] = 0
    if not ukontaktu:
        trci(player, ball['x'], ball['y'])
    else:
        trci_u_krug(player, ball['x'], ball['y'], xzeljeno, yzeljeno)


def vodi_loptu(player, ball, xzeljeno, yzeljeno):
    trci2(player, xzeljeno, yzeljeno, 0.2)


def sutni(player, ball):
    player['shot_request'] = True
    player['shot_power'] = 100000000
    trci(player, ball['x'], ball['y'])


def rastojanje_tacke_od_prave(x1, y1, x2, y2, xt, yt):
    if (x2 == x1):
        a = 1
        b = 0
        c = -x1
    else:
        a = -(y2 - y1) / (x2 - x1)
        b = 1
        c = -y1 + x1 * a
    d = (np.abs(a * xt + b * yt + c)) / (np.sqrt(a ** 2 + b ** 2))
    return d


def provera_da_li_moze_direktno(player, ball, xzeljeno, yzeljeno):
    rl = ball['radius']
    ri = player['radius']
    d0 = rastojanje(player['x'], player['y'], ball['x'], ball['y'])
    dzaproveru = np.sqrt(d0 ** 2 - (rl + ri + 2) ** 2)
    return dzaproveru >= rastojanje(player['x'], player['y'], xzeljeno, yzeljeno)





# def dzoni_prilazak_lopti(player, ball, xz, yz):
#     xi = player['x']
#     yi = player['y']
#     if provera_da_li_moze_direktno(player,ball,)


def gde_se_pozicionirati_za_sut(dribler, ball, our_side, njihov_golman):
    if our_side == 'left':
        xgola = post_screen_right
    else:
        xgola = post_screen_left
    ytop = 50 + int(resolution[1] / 5)
    ybot = resolution[1] - 50
    if njihov_golman['y'] - ytop < ybot - njihov_golman['y']:
        yod = ybot - ball['radius']
        yst = post_screen_bottom - post_radius * 2 - 1
    else:
        yod = ytop + ball['radius']
        yst = post_screen_top + post_radius * 2 + 1

    ylopte = ball['y']
    xlopte = ball['x']

    if (njihov_golman['x'] - njihov_golman['radius'] >= xgola and our_side == 'left') or (
                        njihov_golman['x'] + njihov_golman['radius'] <= xgola and our_side == 'right') or (
                njihov_golman['y'] < ytop) or (njihov_golman['y'] > ybot):
        xod = xgola
        yod = (post_screen_top + post_screen_bottom) / 2
    elif (np.abs(dribler['x'] - xgola) > 0.31 * (post_screen_right - post_screen_left)):
        xod = ((yod - ylopte) * xgola + xlopte * (yod - yst)) / (2 * yod - yst - ylopte)
    else:
        xod = xgola
        if njihov_golman['y'] - ytop < ybot - njihov_golman['y']:
            yod = post_screen_bottom - post_radius * 2 - 1
        else:
            yod = post_screen_top + post_radius * 2 + 1

    d = rastojanje(xlopte, ylopte, xod, yod)
    xzeljeno = xlopte - (dribler['radius'] + ball['radius']) / d * (xod - xlopte)
    yzeljeno = ylopte - (dribler['radius'] + ball['radius']) / d * (yod - ylopte)
    return xzeljeno, yzeljeno


def bloker_trci(dribler, bloker, their_team, ball, our_side):
    R = (dribler['radius'] + bloker['radius']) * 2.379
    niz = []
    i = 0
    while (i < 3):
        if their_team[i]['x'] > dribler['x']:
            niz.append(their_team[i])
        i += 1

    n = i
    i = 1
    ytop = 50 + int(resolution[1] / 5)
    ybot = resolution[1] - 50
    if n == 0:  # cist_gol, samo se skloni gore ili dole, a ovaj dribler ce da puca
        if dribler['y'] < bloker['y']:
            trci(bloker, bloker['x'], ybot + bloker['radius'])
        else:
            trci(bloker, bloker['x'], ytop - bloker['radius'])
    elif n == 1:
        if niz[0]['y'] - ytop < ybot - niz[0]['y']:
            trci(bloker, niz[0]['x'], niz[0]['y'] + bloker['radius'] + 5)
        else:
            trci(bloker, niz[0]['x'], niz[0]['y'] - bloker['radius'] - 5)
    else:
        dmin = rastojanje(dribler['x'], dribler['y'], niz[0]['x'], niz[0]['y'])
        indmin = 0
        while (i < n):
            d = rastojanje(dribler['x'], dribler['y'], niz[i]['x'], niz[i]['y'])
            if d < dmin:
                dmin = d
                indmin = i
            i += 1
        xciljano = dribler['x'] + R / d * (niz[indmin]['x'] - dribler['x'])
        yciljano = dribler['y'] + R / d * (niz[indmin]['y'] - dribler['y'])
        trci(bloker, xciljano, yciljano)


dr_radnja = 0
bl_radnja = 0
strategija = 0
dr_pozicionirao_se = 0


# DRIBLER: 0-trci na loptu; 1-sutni na gol; 2-
# BLOKER: 0-trci na poslednjeg igraca(golmana); 1-

def igraci_zhmk(our_team, their_team, ball, your_side, half, time_left, our_score, their_score):
    global dr_radnja
    global bl_radnja
    strategija = 1
    if strategija == 1:
        return strategija1(our_team, their_team, ball, your_side, half, time_left, our_score, their_score)


def strategija1(our_team, their_team, ball, your_side, half, time_left, our_score,
                their_score):  # bloker na golmanu uvek

    global dr_pozicionirao_se
    bloker = our_team[2]
    dribler = our_team[1]
    if your_side == 'left':
        nasa_strana = 1
        xgola = post_screen_right
    else:
        nasa_strana = -1
        xgola = post_screen_left
    poslednji_igrac = their_team[0]
    if poslednji_igrac['x'] * nasa_strana <= their_team[1]['x'] * nasa_strana and their_team[1][
        'x'] * nasa_strana < xgola * nasa_strana:
        poslednji_igrac = their_team[1]
    if poslednji_igrac['x'] * nasa_strana <= their_team[2]['x'] * nasa_strana and their_team[2][
        'x'] * nasa_strana < xgola * nasa_strana:
        poslednji_igrac = their_team[2]

    bloker_x_zeljeno = poslednji_igrac['x']
    if poslednji_igrac['y'] > (post_screen_bottom + post_screen_top) / 2:
        bloker_y_zeljeno = poslednji_igrac['y'] - (poslednji_igrac['radius'] + bloker['radius'] - 1)
    else:
        bloker_y_zeljeno = poslednji_igrac['y'] + (poslednji_igrac['radius'] + bloker['radius'] - 1)

    trci(bloker, bloker_x_zeljeno, bloker_y_zeljeno)
    bloker['shot_request'] = False
    bloker['shot_power'] = 0

    # BLOKER DA NE IDE VAN TERENA!!!

    if dr_pozicionirao_se == 1:
        sutni(dribler, ball)
        if da_li_je_sutnuta(ball):
            dr_pozicionirao_se = 0
    elif not da_li_je_sutnuta(ball):
        xzelj, yzelj = gde_se_pozicionirati_za_sut(dribler, ball, your_side, poslednji_igrac)
        if np.abs(cm.phase(complex(xzelj - ball['x'], yzelj - ball['y'])) - cm.phase(
                complex(dribler['x'] - ball['x'], dribler['y'] - ball['y']))) <= 0.15 and u_kontaktu(dribler, ball):
            sutni(dribler, ball)
            dr_pozicionirao_se = 1
        else:
            pridji_lopti(dribler, ball, xzelj, yzelj, u_kontaktu(dribler, ball))
    else:
        if np.cos(ball['alpha'] * nasa_strana) > 0:
            # if nasa_strana == 1:
            #     njihov_gol = post_screen_right
            # else:
            #     njihov_gol = post_screen_left

            # y_uci = gde_ce_uci(poslednji_igrac, ball, '', njihov_gol)
            # if not (y_uci < post_screen_bottom and y_uci > post_screen_top):
            #     if ball['x'] * nasa_strana < dribler['x'] * nasa_strana:
            #         y_ceka = gde_ce_uci(dribler, ball, your_side, dribler['x'] - dribler['radius'] * nasa_strana)
            #         po_y_osi(dribler, y_ceka, False)
            #     else:
            #         trci(dribler, ball['x'], ball['y'])
            #         dribler['shot_request'] = False
            #         dribler['shot_power'] = 0
            # else:
            #     trci(dribler, poslednji_igrac['x'], poslednji_igrac['y'])
            #     dribler['shot_request'] = False
            #     dribler['shot_power'] = 0

            y_prati = ball['y']
            x_prati = ball['x'] - nasa_strana * (ball['radius'] + 2 * dribler['radius'])
            trci(dribler, x_prati, y_prati)
            dribler['shot_request'] = False
            dribler['shot_power'] = 0
        else:
            if ball['x'] * nasa_strana > dribler['x'] * nasa_strana:
                y_ceka = gde_ce_uci(dribler, ball, your_side, dribler['x'] - dribler['radius'] * nasa_strana)
                po_y_osi(dribler, y_ceka, False)
            else:
                trci(dribler, center[0], center[1])
                dribler['shot_request'] = False
                dribler['shot_power'] = 0
    if dribler['shot_request']:
        print('nesto')

    return dribler['alpha'], dribler['force'], dribler['shot_request'], dribler['shot_power'], bloker['alpha'], bloker[
        'force'], bloker['shot_request'], bloker['shot_power']


def u_kontaktu(player, ball):
    return (rastojanje(player['x'], player['y'], ball['x'], ball['y']) <= player['radius'] + ball['radius'] + 3)


def decision(our_team, their_team, ball, your_side, half, time_left, our_score, their_score):
    init(our_team, ball)
    manager_decision = [dict(), dict(), dict()]
    for i in range(3):
        player = our_team[i]
        manager_decision[i]['alpha'] = player['alpha']
        manager_decision[i]['force'] = 0
        manager_decision[i]['shot_request'] = False
        manager_decision[i]['shot_power'] = 100000
    manager_decision[0]['alpha'], manager_decision[0]['force'], manager_decision[0]['shot_request'], \
    manager_decision[0]['shot_power'] = golman_zhmk(our_team, their_team, ball, your_side, half, time_left, our_score,
                                                    their_score)
    manager_decision[1]['alpha'], manager_decision[1]['force'], manager_decision[1]['shot_request'], \
    manager_decision[1]['shot_power'], manager_decision[2]['alpha'], manager_decision[2]['force'], manager_decision[2][
        'shot_request'], \
    manager_decision[2]['shot_power'] = igraci_zhmk(our_team, their_team, ball, your_side, half, time_left, our_score,
                                                    their_score)
    return manager_decision
