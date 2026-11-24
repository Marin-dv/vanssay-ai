"""Case study pages for ai.vanssay.net (French). Real content only.

Run through build.py (or directly: python cases.py). Writes cas/<slug>.html.
Support conversations are real, translated from English, with names, sites and accounts removed.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "cas"
SITE = "https://ai.vanssay.net/"
BOOK = "../#contact"

ICONS = {
    "mail": '<path d="M4 6h16v12H4z"/><path d="m4 7 8 6 8-6"/>',
    "layers": '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
    "rocket": '<path d="M12 3c3 2.2 5 6 5 10l-2 3H9l-2-3c0-4 2-7.8 5-10z"/><circle cx="12" cy="10" r="1.7"/><path d="m9.5 16-1.5 4M14.5 16l1.5 4"/>',
    "receipt": '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6M9 16h3"/>',
    "doc": '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/><path d="M10 12h5M10 16h5"/>',
    "shop": '<path d="M4 9 6 4h12l2 5"/><path d="M4 9h16v11H4z"/><path d="M9 20v-6h6v6"/>',
}
COLORS = {"mail": "#2b50ff", "layers": "#7c5cff", "rocket": "#ff7a45", "receipt": "#19c3b1", "doc": "#ff4f9a", "shop": "#0e7afe"}


def icon(name, size=40):
    return (f'<span class="ic" style="background:{COLORS[name]};width:{size}px;height:{size}px">'
            f'<svg viewBox="0 0 24 24" width="{int(size*.5)}" height="{int(size*.5)}" fill="none" stroke="#fff" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg></span>')


NB = " "


def typo(s):
    """French typography: curly apostrophes, non-breaking spaces inside guillemets and before : ; ? !"""
    s = s.replace("'", "’").replace("« ", "«" + NB).replace(" »", NB + "»")
    for p in (":", ";", "?", "!"):
        s = s.replace(" " + p, NB + p)
    return s


def esc(s):
    return html.escape(typo(s), quote=True)


CSS = """
:root { --black:#000; --ink:#101214; --white:#fff; --g1:#f5f5f7; --g2:#ebebed; --g3:#ceced0; --mute:#86868b; --green:#9dff5e;
  --font:"SF Pro Display",-apple-system,BlinkMacSystemFont,"Inter Tight","Inter","Segoe UI",Roboto,sans-serif;
  --pad:max(20px,env(safe-area-inset-left,0px)); --pad-r:max(20px,env(safe-area-inset-right,0px)); color-scheme:light; }
* { box-sizing:border-box; }
:root { padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px); }
body { margin:0; background:var(--white); color:var(--black); font:500 15px/1.5 var(--font); letter-spacing:-.01em; -webkit-font-smoothing:antialiased; }
a { color:inherit; text-decoration:none; }
img, video { display:block; max-width:100%; height:auto; }
h1, h2, h3, p { margin:0; font-weight:500; }
ul, ol { margin:0; padding:0; list-style:none; }
a:focus-visible { outline:2px solid var(--black); outline-offset:3px; border-radius:8px; }
.nav { position:sticky; top:env(safe-area-inset-top,0px); z-index:5; background:rgba(16,18,20,.88); backdrop-filter:blur(14px); -webkit-backdrop-filter:blur(14px); color:var(--white); }
body::before { content:""; position:fixed; inset:0 0 auto; height:env(safe-area-inset-top,0px); background:var(--ink); z-index:6; }
.nav-in { display:flex; align-items:center; justify-content:space-between; gap:16px; padding:12px var(--pad-r) 12px var(--pad); font-size:14px; }
.nav-in .back { opacity:.75; } .nav-in .back:hover { opacity:1; }
.btn { display:inline-flex; align-items:center; justify-content:center; padding:11px 16px; border-radius:8px; font:600 13px/1 var(--font); }
.btn-dark { background:var(--black); color:var(--white); } .btn-dark:hover { background:#2a2a2d; }
.btn-glass { background:rgba(255,255,255,.16); color:var(--white); } .btn-glass:hover { background:rgba(255,255,255,.26); }
.wrap { max-width:1050px; margin:0 auto; padding-left:var(--pad); padding-right:var(--pad-r); }
.head { padding-block:clamp(56px,8vw,110px) clamp(32px,5vw,56px); display:grid; gap:20px; }
.kicker { display:flex; align-items:center; gap:12px; font-size:13px; color:var(--mute); }
.ic { display:inline-grid; place-items:center; border-radius:10px; flex:none; }
.head h1 { font-size:clamp(34px,4.6vw,60px); line-height:1.02; letter-spacing:-.035em; text-wrap:balance; max-width:15em; }
.head .lede { font-size:clamp(18px,1.8vw,22px); line-height:1.35; letter-spacing:-.02em; color:#4a4a4f; max-width:36em; }
.meta { display:flex; flex-wrap:wrap; gap:10px 28px; padding-top:8px; border-top:1px solid var(--g2); font-size:14px; }
.meta div { display:grid; gap:2px; padding-top:12px; } .meta span { font-size:12px; color:var(--mute); }
.cover { border-radius:12px; overflow:hidden; background:var(--g1); margin-bottom:clamp(40px,6vw,72px); }
.cover img, .cover video { width:100%; aspect-ratio:16/8; object-fit:cover; }
.gallery { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-bottom:clamp(40px,6vw,72px); }
.gallery img { border-radius:12px; aspect-ratio:1; object-fit:cover; width:100%; }
section.block { display:grid; grid-template-columns:1fr 2fr; gap:clamp(20px,5vw,80px); padding-block:clamp(36px,5vw,64px); border-top:1px solid var(--g2); }
section.block > h2 { font-size:13px; color:var(--mute); letter-spacing:0; }
.prose { display:grid; gap:16px; font-size:clamp(18px,1.6vw,21px); line-height:1.42; letter-spacing:-.02em; }
.prose p.small { font-size:15px; color:var(--mute); letter-spacing:-.01em; }
.steps { display:grid; gap:0; counter-reset:s; }
.steps li { display:grid; grid-template-columns:36px 1fr; gap:12px; padding:14px 0; border-top:1px solid var(--g2); counter-increment:s; font-size:17px; line-height:1.4; }
.steps li:first-child { border-top:0; padding-top:0; }
.steps li::before { content:counter(s); font-size:13px; color:var(--mute); padding-top:3px; }
.steps b { font-weight:600; }
.facts { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }
.fact { background:var(--g1); border-radius:12px; padding:20px; display:grid; gap:6px; }
.fact b { font-size:clamp(28px,3vw,40px); font-weight:500; letter-spacing:-.035em; line-height:1; }
.fact span { font-size:13px; color:#6e6e73; }
.notes li { padding:12px 16px; background:var(--g1); border-radius:10px; font-size:15px; margin-bottom:8px; }
.notes li span { color:var(--mute); }
.conv { display:grid; gap:12px; margin-bottom:28px; }
.conv h3 { font-size:22px; letter-spacing:-.025em; margin-bottom:4px; }
.msg { border-radius:14px; padding:16px 18px; display:grid; gap:8px; font-size:16px; line-height:1.45; max-width:44em; }
.msg .who { font-size:12px; color:var(--mute); display:flex; gap:8px; align-items:center; }
.msg.in { background:var(--g1); }
.msg.out { background:var(--ink); color:var(--white); margin-left:auto; }
.msg.out .who { color:#a1a1a6; }
.msg.thanks { background:#eef9e6; max-width:30em; }
.work { border:1px dashed var(--g3); border-radius:14px; padding:16px 18px; display:grid; gap:10px; }
.work .who { font-size:12px; color:var(--mute); }
.work li { display:grid; grid-template-columns:18px 1fr; gap:10px; font-size:15px; line-height:1.4; }
.work li::before { content:""; width:8px; height:8px; border-radius:50%; background:#2b50ff; margin-top:7px; }
.timing { font-size:13px; color:var(--mute); }
.cta { background:var(--ink); color:var(--white); margin-top:clamp(40px,6vw,80px); }
.cta-in { display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:20px; padding-block:clamp(48px,7vw,90px); }
.cta h2 { font-size:clamp(26px,3vw,40px); letter-spacing:-.03em; line-height:1.08; max-width:18em; }
.more { padding-block:clamp(40px,6vw,72px); }
.more h2 { font-size:24px; letter-spacing:-.025em; margin-bottom:18px; }
.more-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(230px,1fr)); gap:10px; }
.more-grid a { display:flex; align-items:center; gap:12px; background:var(--g1); border-radius:12px; padding:14px 16px; }
.more-grid a:hover { background:var(--g2); }
.more-grid b { font-weight:500; display:block; } .more-grid span span { font-size:13px; color:var(--mute); }
footer { padding:28px var(--pad-r) 28px var(--pad); font-size:13px; color:var(--mute); display:flex; flex-wrap:wrap; justify-content:space-between; gap:8px 24px; }
@media (max-width:760px) { section.block { grid-template-columns:1fr; } .facts, .gallery { grid-template-columns:1fr 1fr; } }
@media (max-width:480px) { .facts, .gallery { grid-template-columns:1fr; } }
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
            "Le même principe s'applique à n'importe quelle PME : un fichier qui décrit votre métier, vos règles et votre ton, que l'IA lit avant chaque tâche. C'est ce qu'on a installé chez Le Typographe.",
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
            "L'IA lit les notices, remplit et rédige. Je relis chaque ligne et c'est moi qui envoie. Pour une PME, c'est la même chose avec les déclarations, les relances ou les dossiers de subvention.",
        ]),
    ],
)


def render_block(title, kind, items):
    if kind == "steps":
        inner = '<ol class="steps">' + "".join(f"<li><div>{typo(i)}</div></li>" for i in items) + "</ol>"
    elif kind == "notes":
        inner = '<ul class="notes">' + "".join(f"<li>{esc(a)} <span>· {esc(b)}</span></li>" for a, b in items) + "</ul>"
    else:
        inner = '<div class="prose">' + "".join(typo(i) if i.startswith("<p") else f"<p>{typo(i)}</p>" for i in items) + "</div>"
    return f'<section class="block wrap"><h2>{esc(title)}</h2>{inner}</section>'


def render_conv(c):
    work = "".join(f"<li><div>{esc(w)}</div></li>" for w in c["work"])
    timing = f'<p class="timing">{esc(c["timing"])}</p>' if c.get("timing") else ""
    return f"""<div class="conv">
  <h3>{esc(c['title'])}</h3>
  <div class="msg in"><span class="who">Le client</span><p>{esc(c['client'])}</p></div>
  <div class="work"><span class="who">Ce que l'IA a vérifié et fait avant de répondre</span><ul>{work}</ul></div>
  <div class="msg out"><span class="who">Réponse, relue par moi puis envoyée</span><p>{esc(c['reply'])}</p></div>
  <div class="msg thanks"><span class="who">Le client</span><p>{esc(c['thanks'])}</p></div>
  {timing}
</div>"""


def page(c):
    meta = "".join(f"<div><span>{esc(k)}</span>{esc(v)}</div>" for k, v in c["meta"])
    media = ""
    if c.get("cover_video"):
        src, poster = c["cover_video"]
        media = f'<div class="wrap"><div class="cover"><video autoplay muted loop playsinline poster="{poster}"><source src="{src}" type="video/mp4"></video></div></div>'
    if c.get("gallery"):
        media = '<div class="wrap"><div class="gallery">' + "".join(f'<img src="{g}" alt="" loading="lazy">' for g in c["gallery"]) + "</div></div>"
    body = "".join(render_block(*b) for b in c.get("blocks", []))
    if c.get("conversations"):
        convs = "".join(render_conv(x) for x in c["conversations"])
        body += f'<section class="block wrap"><h2>Deux vrais échanges</h2><div>{convs}<p class="timing">{esc(c["conv_note"])}</p></div></section>'
    if c.get("facts"):
        facts = "".join(f'<div class="fact"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a, b in c["facts"])
        body += f'<section class="block wrap"><h2>En chiffres</h2><div class="facts">{facts}</div></section>'
    body += "".join(render_block(*b) for b in c.get("after", []))
    others = "".join(
        f'<a href="{o["slug"]}.html">{icon(o["icon"], 36)}<span><b>{esc(o["short"])}</b><span>{esc(o["sub"])}</span></span></a>'
        for o in CASES if o["slug"] != c["slug"])
    title = f"{c['short']} · Étude de cas · Marin de Vanssay"
    desc = c["lede"]
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}cas/{c['slug']}.html">
<link rel="icon" href="/favicon.ico" sizes="any">
<meta property="og:type" content="article">
<meta property="og:title" content="{esc(c['title'])}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE}img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600&display=swap">
<style>{CSS}</style>
</head>
<body>
<header class="nav"><div class="nav-in"><a class="back" href="../#travaux">← Marin de Vanssay</a><a class="btn btn-glass" href="{BOOK}">Réserver un appel</a></div></header>
<main>
  <div class="wrap head">
    <p class="kicker">{icon(c['icon'])}Étude de cas</p>
    <h1>{esc(c['title'])}</h1>
    <p class="lede">{esc(c['lede'])}</p>
    <div class="meta">{meta}</div>
  </div>
  {media}
  {body}
  <section class="cta"><div class="wrap cta-in"><h2>Une tâche comme celle-ci dans votre équipe&nbsp;?</h2><a class="btn btn-glass" href="{BOOK}">Réserver un appel de 15&nbsp;min</a></div></section>
  <section class="wrap more"><h2>Autres études de cas</h2><div class="more-grid">{others}</div></section>
</main>
<footer><span>Vanssay · Marin de Vanssay © 2026</span><a href="../">ai.vanssay.net</a></footer>
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
