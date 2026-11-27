"""Case study pages for ai.vanssay.net (French). Real content only.

Run through build.py (or directly: python cases.py). Writes cas/<slug>.html.
The pages reuse the home page's own style, header, footer and scripts (read from page.html),
so they always look like the home page. The call-to-action band uses the hero's live canvas.
Support conversations are real, translated from English, with names, sites and accounts removed.
Thumbnails are existing assets only (product icons, crops of existing visuals), never drawn icons.
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "cas"
SITE = "https://ai.vanssay.net/"

THUMBS = {
    "mail": "ic-support.png",      # Reviews app icon with the Vanssay badge (a message bubble)
    "shop": "lt-shop.webp",        # Le Typographe's shop (their Instagram photo)
    "layers": "ic-vanssay.png",    # Vanssay glyph (the company's own memory)
    "rocket": "ic-2027.png",       # Google Reviews 2027 app icon
    "receipt": "ic-billing.png",   # the real subscription email's button
    "doc": "ic-cfe.png",           # CFE cartouche from the blank tax form
}


def thumb(name, cls="av"):
    return f'<img class="{cls}" src="../img/{THUMBS[name]}" alt="">'


NB = " "


def typo(s):
    """French typography: curly apostrophes, non-breaking spaces inside guillemets and before : ; ? !"""
    s = s.replace("'", "’").replace("« ", "«" + NB).replace(" »", NB + "»")
    for p in (":", ";", "?", "!"):
        s = s.replace(" " + p, NB + p)
    return s


def esc(s):
    return html.escape(typo(s), quote=True)


# ---------------------------------------------------------------- pieces of the home page
HOME = (ROOT / "page.html").read_text(encoding="utf-8")
HOME_STYLE = re.search(r"<style>(.*?)</style>", HOME, re.S).group(1)
HOME_FONTS = "\n".join(l for l in HOME.splitlines() if "fonts.g" in l)
HOME_TOP = re.search(r'(<header class="nav".*?</aside>)', HOME, re.S).group(1)
HOME_FOOTER = re.search(r'(<footer id="contact">.*?</footer>)', HOME, re.S).group(1)
HOME_SCRIPT = re.search(r"(<script>.*?</script>)", HOME, re.S).group(1)


def relink(s):
    """Home page links and assets, seen from cas/<slug>.html."""
    s = s.replace('href="#top"', 'href="../"')
    for a in ("methodes", "travaux", "services", "tarifs"):
        s = s.replace(f'href="#{a}"', f'href="../#{a}"')
    s = s.replace('href="cas/', 'href="')
    s = s.replace('src="img/', 'src="../img/')
    return s


CASE_CSS = """
.case .nav { background: rgba(16, 18, 20, .72); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); }
.c-wrap { max-width: 1050px; margin: 0 auto; padding-left: var(--pad); padding-right: var(--pad-r); }
.hero.c-strip { height: clamp(150px, 16vw, 220px); min-height: 0; }
.c-head { padding-top: clamp(48px, 6vw, 84px); padding-bottom: clamp(40px, 5vw, 64px); display: grid; gap: 22px; }
.c-kicker { display: flex; align-items: center; gap: 12px; }
.c-kicker .av { width: 40px; height: 40px; border-radius: 8px; object-fit: cover; }
.c-head h1 { font-size: clamp(34px, 3.6vw, 52px); line-height: 1.04; letter-spacing: -.03em; max-width: 15em; text-wrap: balance; }
.c-lede { font-size: clamp(22px, 2.1vw, 30px); line-height: 1.22; letter-spacing: -.025em; color: #3a3a3c; max-width: 30em; }
.c-meta { display: flex; flex-wrap: wrap; gap: 8px; }
.c-meta div { background: var(--g1); border-radius: 10px; padding: 10px 14px; display: grid; gap: 2px; font-size: 14px; }
.c-meta span { font-size: 12px; color: var(--mute); }
.c-media { margin-bottom: clamp(48px, 7vw, 96px); }
.c-media .cover { border-radius: 12px; overflow: hidden; background: var(--ink); }
.c-media .cover video, .c-media .cover img { width: 100%; aspect-ratio: 16 / 8; object-fit: cover; }
.c-gallery { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
.c-gallery img { width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 12px; }
.c-block { display: grid; grid-template-columns: 1fr 2fr; gap: clamp(24px, 6vw, 110px); padding-bottom: clamp(48px, 7vw, 96px); }
.c-block > div { display: grid; gap: 8px; min-width: 0; align-content: start; }
.c-steps { display: grid; gap: 8px; counter-reset: s; }
.c-steps li { display: grid; grid-template-columns: 28px 1fr; gap: 10px; background: var(--g1); border-radius: 12px; padding: 15px 16px; font-size: 16px; line-height: 1.42; counter-increment: s; }
.c-steps li::before { content: counter(s); color: var(--mute); font-size: 14px; }
.c-steps b { font-weight: 600; }
.c-prose { display: grid; gap: 14px; }
.c-prose p { font-size: clamp(20px, 1.9vw, 26px); line-height: 1.25; letter-spacing: -.025em; }
.c-prose p.small { font-size: 15px; color: var(--mute); letter-spacing: -.01em; }
.c-notes { display: grid; gap: 8px; }
.c-notes li { background: var(--g1); border-radius: 12px; padding: 15px 16px; display: grid; gap: 2px; }
.c-notes li span { color: var(--mute); font-size: 15px; }
.c-conv { display: grid; gap: 8px; margin-bottom: 40px; }
.c-conv h3 { font-size: 24px; letter-spacing: -.025em; margin-bottom: 6px; }
.c-msg { border-radius: 12px; padding: 16px 18px; display: grid; gap: 8px; font-size: 17px; line-height: 1.42; letter-spacing: -.015em; }
.c-msg .who { font-size: 12px; color: var(--mute); letter-spacing: 0; }
.c-msg.in { background: var(--g1); }
.c-msg.out { background: var(--black); color: var(--white); }
.c-msg.out .who { color: #a1a1a6; }
.c-work { background: var(--g2); border-radius: 12px; padding: 16px 18px; display: grid; gap: 10px; }
.c-work .who { font-size: 12px; color: var(--mute); }
.c-work ul { display: grid; gap: 6px; }
.c-work li { display: flex; gap: 10px; align-items: baseline; font-size: 15px; line-height: 1.4; color: #3a3a3c; }
.c-work li::before { content: ""; width: 5px; height: 5px; border-radius: 50%; background: #8e8e93; flex: none; transform: translateY(-2px); }
.c-msg.thanks { background: var(--g1); max-width: 34em; }
.c-timing { font-size: 13px; color: var(--mute); }
.c-facts { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
.c-fact { background: var(--g1); border-radius: 12px; padding: 20px; display: grid; gap: 10px; align-content: start; }
.c-fact b { font-size: clamp(38px, 3.2vw, 48px); font-weight: 500; letter-spacing: -.035em; line-height: 1; font-variant-numeric: tabular-nums; }
.c-fact span { font-size: 14px; color: #6e6e73; }
.hero.c-cta { height: clamp(380px, 46vw, 520px); min-height: 0; }
.hero.c-cta h1 { max-width: 20em; }
.c-others { padding-block: clamp(56px, 8vw, 110px); }
.c-others-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; }
.c-other { display: grid; grid-template-columns: 40px 1fr 30px; align-items: center; gap: 12px; background: var(--g1); border-radius: 12px; padding: 15px 16px; }
.c-other:hover { background: var(--g2); }
.c-other .av { width: 40px; height: 40px; border-radius: 8px; object-fit: cover; }
.c-other .go { justify-self: end; width: 30px; height: 30px; border-radius: 50%; background: var(--white); display: grid; place-items: center; font-size: 15px; color: #6e6e73; }
@media (max-width: 760px) { .c-block { grid-template-columns: 1fr; } .c-facts, .c-gallery { grid-template-columns: 1fr 1fr; } .c-others-grid { grid-template-columns: 1fr; } }
@media (max-width: 480px) { .c-facts, .c-gallery { grid-template-columns: 1fr; } }
"""

CASES = []


def case(**kw):
    CASES.append(kw)


# ---------------------------------------------------------------- support
case(
    slug="support-client", icon="mail", short="Support client", sub="L'IA fait l'enquête, je relis",
    title="Support client : l'IA fait l'enquête, je relis et j'envoie.",
    lede="Dans ma propre entreprise, chaque mail client passe par une routine IA. Elle retrouve le compte, vérifie le problème sur le vrai produit, corrige quand elle peut, puis rédige la réponse. Je relis, j'envoie.",
    meta=[("Entreprise", "Vanssay, la mienne"), ("Outils", "Claude, Gmail, mes serveurs"), ("Avant chaque envoi", "Relu par moi")],
    blocks=[
        ("Comment ça marche", "steps", [
            "<b>Le mail arrive</b> sur l'adresse du support. Claude le lit dans Gmail et le classe.",
            "<b>Il retrouve le client</b> : son compte, son abonnement, son site.",
            "<b>Il vérifie le problème</b> sur le vrai produit et les vraies données du client, pas sur une supposition.",
            "<b>S'il peut corriger, il corrige</b>, et note la correction définitive pour la prochaine version.",
            "<b>Il rédige la réponse</b> dans mon ton. Je la relis, puis je l'envoie.",
        ]),
    ],
    conversations=[
        dict(
            title="Un badge Trustpilot bloqué sur « Great »",
            client="Bonjour, le badge Trustpilot de mon site ne passe pas de « Great » (vert clair) à « Excellent » (vert émeraude). Ma note Trustpilot est de 4,4, le badge devrait donc changer. Comment corriger ça ?",
            work=[
                "Le site et le compte du client, et sa note publique sur Trustpilot : 4,4.",
                "Les paliers officiels de Trustpilot : « Excellent » commence à 4,3.",
                "Le code du badge : il ne passait à « Excellent » qu'à partir de 4,5. Le bug venait de chez nous.",
                "Correction appliquée tout de suite pour le site du client, correction définitive ajoutée à la prochaine version du plugin.",
            ],
            reply="Bonjour, merci de l'avoir signalé, c'est réglé. Votre badge affiche maintenant « Excellent » en vert émeraude, comme sur votre profil Trustpilot. Vous n'avez rien à faire. Vous aviez raison, le problème venait de chez nous : Trustpilot classe « Excellent » tout ce qui est à partir de 4,3, mais notre badge ne changeait qu'à 4,5. Je l'ai corrigé pour votre site, et la correction définitive arrive dans la prochaine version du plugin.",
            thanks="Super nouvelle, merci d'avoir réglé ça si vite !",
            timing=None,
        ),
        dict(
            title="Un fil Instagram qui n'affiche pas les derniers posts",
            client="Bonjour, nous venons d'acheter l'abonnement à vie du plugin Instagram Feed, mais la synchronisation automatique n'affiche pas les posts les plus récents de notre compte. Y a-t-il une solution rapide ?",
            work=[
                "Le fil du client sur son site, comparé à son compte Instagram : les derniers posts manquaient.",
                "Les données du fil sur le serveur : les posts étaient servis dans le mauvais ordre, les plus anciens d'abord.",
                "Correction de l'ordre, puis vérification sur le site en ligne : les derniers posts apparaissent en premier.",
                "Le client a l'offre à vie, qui se met à jour une fois par semaine : la réponse explique le bouton « Synchroniser maintenant ».",
            ],
            reply="Bonjour, merci pour le signalement et pour les détails. Vous aviez raison, il y avait un problème de notre côté : les posts de votre compte étaient servis dans le mauvais ordre. C'est corrigé, votre site affiche maintenant vos derniers posts en premier ; rechargez simplement la page. À savoir avec l'offre à vie : le fil se met à jour automatiquement une fois par semaine. Pour afficher un nouveau post tout de suite, ouvrez le tableau de bord du plugin et cliquez sur « Synchroniser maintenant ».",
            thanks="Merci pour la réponse rapide. Tout fonctionne parfaitement maintenant !",
            timing="Réponse envoyée 2 h 30 après le mail du client. Sa confirmation est arrivée 3 minutes plus tard.",
        ),
    ],
    conv_note="Conversations réelles, traduites de l'anglais. Noms, sites et comptes retirés.",
    after=[
        ("Ce que ça change", "prose", [
            "Chaque réponse part avec un diagnostic vérifié sur le vrai produit, pas avec une supposition.",
            "Quand c'est un bug, il est corrigé pendant la réponse, pas une semaine plus tard.",
            "Je garde la main : rien ne part sans ma relecture.",
            "<p class=\"small\">La même routine peut lire votre boîte de réception, vos commandes ou votre CRM, selon vos outils.</p>",
        ]),
    ],
)

# ---------------------------------------------------------------- le typographe
case(
    slug="le-typographe", icon="shop", short="Le Typographe", sub="Claude installé en un après-midi",
    title="Le Typographe : Claude installé en un après-midi.",
    lede="Une papeterie haut de gamme à Bruxelles, avec près de 900 produits en ligne. En un après-midi avec la gérante, l'IA est passée d'un outil inconnu à un assistant qui connaît la boutique.",
    meta=[("Client", "Le Typographe, Bruxelles"), ("Durée", "Un après-midi"), ("Outils", "Claude, Gmail, Claude dans Chrome, WordPress")],
    gallery=["../img/lt-shop.webp", "../img/lt-notebooks.webp", "../img/wix-aria.webp"],
    blocks=[
        ("Le point de départ", "prose", [
            "La boutique en ligne compte environ 880 produits, chacun en français et en anglais : 1 765 fiches produits.",
            "Mettre ces fiches à jour à la main prenait des heures. Et la moindre correction sur le site passait par le développeur.",
        ]),
        ("Ce qu'on a fait", "steps", [
            "<b>Sa boîte mail connectée à Claude</b>, pour qu'il lise et rédige à partir de ses vrais mails.",
            "<b>Claude ajouté dans Chrome</b>, pour qu'il agisse directement sur les pages qu'elle ouvre.",
            "<b>Quatre pages du site WordPress corrigées</b> en quelques minutes, au lieu de plusieurs heures.",
            "<b>Un fichier qui décrit la boutique</b> : son métier, son éthique, son goût visuel. Claude le lit avant chaque tâche.",
            "<b>Des routines pour les tâches répétitives</b>, comme la mise à jour des fiches produits.",
        ]),
        ("Ce qui reste chez elle", "prose", [
            "Tout est installé dans ses propres outils : les connexions, le fichier de la boutique et les routines. Rien ne dépend de moi pour fonctionner.",
        ]),
    ],
    facts=[("880", "produits en ligne"), ("1 765", "fiches produits, en français et en anglais"), ("1", "après-midi d'installation")],
)

# ---------------------------------------------------------------- memoire
case(
    slug="memoire", icon="layers", short="Mémoire de l'entreprise", sub="77 notes, 30 routines",
    title="Mémoire de l'entreprise : mon IA connaît déjà Vanssay.",
    lede="Une IA qui repart de zéro à chaque conversation fait perdre du temps : il faut tout réexpliquer. Chez moi, elle démarre chaque séance en sachant déjà comment l'entreprise fonctionne.",
    meta=[("Entreprise", "Vanssay, la mienne"), ("Contenu", "77 notes, 30 routines"), ("Mise à jour", "À la fin de chaque séance")],
    blocks=[
        ("Comment ça marche", "steps", [
            "<b>Un fichier décrit l'entreprise</b> : les produits, où ils tournent, les règles à ne jamais enfreindre.",
            "<b>Des notes gardent les décisions</b> et leur raison : pourquoi tel prix, pourquoi tel refus, ce qui a cassé et comment on l'a réparé.",
            "<b>Des routines décrivent les tâches répétées</b> pas à pas : répondre au support, mettre en ligne, créer un tarif.",
            "<b>En fin de séance</b>, l'IA note où on en est, pour que la suivante reprenne au bon endroit.",
        ]),
        ("Extraits réels", "notes", [
            ("Règles de validation Webflow", "à lire avant toute modification d'une application Webflow"),
            ("Mise en ligne de Router", "toujours sur son propre projet, sinon elle coupe Bouncer"),
            ("Comptes de démonstration", "toujours sur la meilleure offre, jamais sur l'offre gratuite"),
            ("Factures", "une seule série numérotée, jamais de numéro à la main"),
            ("Fiche Google de Le Typographe", "lecture seule, on ne modifie jamais rien"),
        ]),
        ("Pour votre entreprise", "prose", [
            "Le même principe s'applique à n'importe quelle entreprise, même d'une seule personne : un fichier qui décrit votre métier, vos règles et votre ton, que l'IA lit avant chaque tâche. C'est ce qu'on a installé chez Le Typographe.",
        ]),
    ],
)

# ---------------------------------------------------------------- mises en ligne
case(
    slug="mises-en-ligne", icon="rocket", short="Mises en ligne", sub="Une application Wix en deux jours",
    title="Mises en ligne : une application Wix en deux jours.",
    lede="Entre la décision de sortir mon produit d'avis Google sur Wix et une application en production, prête à être soumise, il s'est passé deux jours. Chaque étape sensible attend mon accord.",
    meta=[("Produit", "Google Reviews 2027, pour Wix"), ("Durée", "Du 12 au 14 novembre 2026"), ("Garde-fou", "Mon accord à chaque étape")],
    cover_video=("../img/wix-promo.mp4", "../img/wix-promo-poster.jpg"),
    blocks=[
        ("Le calendrier", "steps", [
            "<b>12 novembre</b> : choix de Wix comme prochaine plateforme, étude du marché et cahier des charges.",
            "<b>13 novembre</b> : serveur en production, premières versions de l'application installées sur un site test.",
            "<b>14 novembre</b> : version 2.1.0, avec fiche, visuels et vidéo de présentation prêts pour la soumission.",
        ]),
        ("La routine de mise en ligne", "steps", [
            "<b>Périmètre</b> : la liste exacte de ce qui part en ligne.",
            "<b>Vérification</b> que rien de ce que les sites clients utilisent ne casse.",
            "<b>Tests</b> sur chaque partie du produit.",
            "<b>Sauvegarde</b> de la base de données avant de toucher à la production.",
            "<b>Déploiement</b> du serveur, avec contrôle de son état.",
            "<b>Test en production</b>, sur le vrai service.",
            "<b>Publication</b> de la nouvelle version du plugin.",
        ]),
        ("Le principe", "prose", [
            "L'IA prépare et exécute chaque étape, mais elle s'arrête et me montre le résultat avant de passer à la suivante. Rien ne part en production sans mon accord.",
        ]),
    ],
)

# ---------------------------------------------------------------- facturation
case(
    slug="facturation", icon="receipt", short="Facturation", sub="Factures et ventes, sans moi",
    title="Facturation : les factures se font toutes seules.",
    lede="Chaque paiement déclenche la suite tout seul : la facture, son numéro, la TVA, et la vente dans mon tableau de bord. Je n'y touche pas.",
    meta=[("Entreprise", "Vanssay, la mienne"), ("Outils", "Stripe, mon serveur, un tableau de bord"), ("Mon rôle", "Vérifier, pas saisir")],
    blocks=[
        ("Ce qui se passe à chaque paiement", "steps", [
            "<b>Le client paie</b> son abonnement ou son achat.",
            "<b>La facture est émise</b> avec le numéro suivant d'une seule série, sans trou.",
            "<b>La TVA est appliquée</b> selon le pays et le statut du client, y compris l'autoliquidation pour les entreprises européennes.",
            "<b>Le client télécharge ses factures</b> lui-même depuis son compte.",
            "<b>La vente apparaît</b> dans mon tableau de bord, avec les inscriptions et l'usage de chaque produit.",
        ]),
        ("Pourquoi c'est important", "prose", [
            "Une série de factures doit rester continue, et une erreur de TVA coûte cher. Tout ce qui est répétitif et réglementé est exactement ce qu'il faut confier à une routine, puis vérifier.",
        ]),
    ],
)

# ---------------------------------------------------------------- administratif
case(
    slug="administratif", icon="doc", short="Administratif", sub="Même les impôts",
    title="Administratif : même les impôts.",
    lede="Les démarches d'une micro-entreprise prennent du temps, et une erreur se paie. L'IA les prépare avec moi, je vérifie et j'envoie.",
    meta=[("Entreprise", "Vanssay, la mienne"), ("Outils", "Claude, les sites des impôts et des douanes"), ("Envoi", "Toujours par moi")],
    blocks=[
        ("Ce qu'on a préparé ensemble", "steps", [
            "<b>La déclaration initiale de CFE</b> (formulaire 1447-C-K), remplie et envoyée au service des impôts en novembre 2026.",
            "<b>La demande de numéro de TVA intracommunautaire</b>, pour facturer les entreprises européennes.",
            "<b>Les déclarations européennes de services</b> auprès des douanes, pour les ventes à des entreprises de l'Union européenne.",
            "<b>Les courriers au service des impôts</b>, rédigés à partir de mes notes.",
        ]),
        ("La règle", "prose", [
            "L'IA lit les notices, remplit et rédige. Je relis chaque ligne et c'est moi qui envoie. Pour un indépendant ou une PME, c'est la même chose avec les déclarations, les relances ou les dossiers de subvention.",
        ]),
    ],
)


def render_block(title, kind, items):
    if kind == "steps":
        inner = '<ol class="c-steps">' + "".join(f"<li><div>{typo(i)}</div></li>" for i in items) + "</ol>"
    elif kind == "notes":
        inner = '<ul class="c-notes">' + "".join(f"<li><b>{esc(a)}</b><span>{esc(b)}</span></li>" for a, b in items) + "</ul>"
    else:
        inner = '<div class="c-prose">' + "".join(typo(i) if i.startswith("<p") else f"<p>{typo(i)}</p>" for i in items) + "</div>"
    return f'<section class="c-wrap c-block"><p class="label">{esc(title)}</p><div>{inner}</div></section>'


def render_conv(c):
    work = "".join(f"<li>{esc(w)}</li>" for w in c["work"])
    timing = f'<p class="c-timing">{esc(c["timing"])}</p>' if c.get("timing") else ""
    return f"""<div class="c-conv">
  <h3>{esc(c['title'])}</h3>
  <div class="c-msg in"><span class="who">Le client</span><p>{esc(c['client'])}</p></div>
  <div class="c-work"><span class="who">Ce que l'IA a vérifié et fait avant de répondre</span><ul>{work}</ul></div>
  <div class="c-msg out"><span class="who">Réponse, relue par moi puis envoyée</span><p>{esc(c['reply'])}</p></div>
  <div class="c-msg thanks"><span class="who">Le client</span><p>{esc(c['thanks'])}</p></div>
  {timing}
</div>"""


def page(c):
    meta = "".join(f"<div><span>{esc(k)}</span>{esc(v)}</div>" for k, v in c["meta"])
    media = ""
    if c.get("cover_video"):
        src, poster = c["cover_video"]
        media = f'<div class="c-wrap c-media"><div class="cover"><video autoplay muted loop playsinline poster="{poster}"><source src="{src}" type="video/mp4"></video></div></div>'
    if c.get("gallery"):
        media = '<div class="c-wrap c-media"><div class="c-gallery">' + "".join(f'<img src="{g}" alt="" loading="lazy">' for g in c["gallery"]) + "</div></div>"
    body = "".join(render_block(*b) for b in c.get("blocks", []))
    if c.get("conversations"):
        convs = "".join(render_conv(x) for x in c["conversations"])
        body += f'<section class="c-wrap c-block"><p class="label">Deux vrais échanges</p><div>{convs}<p class="c-timing">{esc(c["conv_note"])}</p></div></section>'
    if c.get("facts"):
        facts = "".join(f'<div class="c-fact"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in c["facts"])
        body += f'<section class="c-wrap c-block"><p class="label">En chiffres</p><div class="c-facts">{facts}</div></section>'
    body += "".join(render_block(*b) for b in c.get("after", []))
    others = "".join(
        f'<a class="c-other" href="{o["slug"]}.html">{thumb(o["icon"])}<span class="who"><b>{esc(o["short"])}</b><span>{esc(o["sub"])}</span></span><span class="go" aria-hidden="true">→</span></a>'
        for o in CASES if o["slug"] != c["slug"])
    title = f"{c['short']} · Étude de cas · Marin de Vanssay"
    desc = typo(c["lede"])
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{SITE}cas/{c['slug']}.html">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="apple-touch-icon" href="/favicon-180.png">
<meta property="og:type" content="article">
<meta property="og:url" content="{SITE}cas/{c['slug']}.html">
<meta property="og:title" content="{esc(c['title'])}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:image" content="{SITE}img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}[hidden]{{display:none!important}}</style>
{HOME_FONTS}
<style>{HOME_STYLE}{CASE_CSS}</style>
</head>
<body class="case">
{relink(HOME_TOP)}
<main>
  <section class="hero c-strip" aria-hidden="true">
    <canvas class="hero-media"></canvas>
    <div class="hero-grain"></div>
    <div class="hero-shade"></div>
  </section>
  <section class="c-wrap c-head" id="top">
    <p class="c-kicker">{thumb(c['icon'])}<span class="label">Étude de cas</span></p>
    <h1>{esc(c['title'])}</h1>
    <p class="c-lede">{esc(c['lede'])}</p>
    <div class="c-meta">{meta}</div>
  </section>
  {media}
  {body}
  <section class="hero c-cta" aria-label="Réserver un appel">
    <canvas class="hero-media" id="heroCanvas" aria-hidden="true"></canvas>
    <div class="hero-grain" aria-hidden="true"></div>
    <div class="hero-shade"></div>
    <div class="hero-in">
      <h1>Une tâche comme celle‑ci chez vous&nbsp;?</h1>
      <a class="btn btn-glass" href="https://calendly.com/marindv-pro/appel-decouverte" target="_blank" rel="noopener">Réserver un appel de 15&nbsp;min</a>
    </div>
  </section>
  <section class="c-wrap c-others">
    <div class="row-head"><h2>Autres études de cas</h2><p><a href="../#cas">Tous les cas concrets</a></p></div>
    <div class="c-others-grid">{others}</div>
  </section>
</main>
{relink(HOME_FOOTER)}
{HOME_SCRIPT}
</body>
</html>
"""


def build():
    OUT.mkdir(exist_ok=True)
    for c in CASES:
        (OUT / f"{c['slug']}.html").write_text(page(c), encoding="utf-8")
    return [c["slug"] for c in CASES]


if __name__ == "__main__":
    print("cases:", ", ".join(build()))
