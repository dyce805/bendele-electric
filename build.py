#!/usr/bin/env python3
"""Generates every page of the Bendele Electric site into the repo root.

Shared header, footer and business details live here so they are written once.
Edit the content below (or the fragments in content/), then run:

    python3 build.py
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://bendele-electric.com"   # change here when the domain is decided
NAME = "Bendele Electric Inc."
PHONE = "(805) 287-9044"
TEL = "+18052879044"
FAX = "(805) 764-8636"
EMAIL = "anthony@bendeleelectric.com"
LICENSE = "881830"
YEARS = "20"
HOURS = "Mon&ndash;Fri 7:00 AM&ndash;3:30 PM"
FONTS = "family=Barlow+Condensed:wght@600;800&family=Barlow:wght@400;600"

# name: (width, height) of the large file
PHOTOS = {
    "truck": (1170, 878), "fleet": (1600, 1200), "lift": (1600, 1200), "slab": (1600, 1200),
    "conduit": (1200, 1600), "warehouse": (1200, 1600), "trenching": (1200, 1600),
    "pedestal": (1200, 1600),
}
# name: (caption, alt text)
PHOTO_TEXT = {
    "truck": ("One of our service trucks hauling the lift to a job.",
              "Bendele Electric service truck towing a scissor lift past a Santa Maria Valley vineyard"),
    "fleet": ("Both trucks on a job site.", "Two Bendele Electric service trucks parked at a job site"),
    "lift": ("Running conduit to a warehouse electrical room.",
             "Bendele Electric electrician on a scissor lift bending conduit outside a warehouse electrical room"),
    "conduit": ("Racked conduit runs in a commercial building.",
                "Electrician on a scissor lift installing racked conduit runs along a block wall"),
    "slab": ("Underground conduit stubbed up before a slab pour.",
             "Underground electrical conduit stubbed up through rebar before a concrete slab pour"),
    "trenching": ("Trenching a parking lot for new underground power.",
                  "Bendele Electric crew member trenching across a parking lot for underground conduit"),
    "warehouse": ("Equipment hookup on a warehouse floor.",
                  "Bendele Electric electrician wiring equipment on a warehouse floor"),
    "pedestal": ("New power pedestal with 50 and 30 amp outlets.",
                 "Newly installed outdoor power pedestal with 50 amp and 30 amp receptacles"),
}
WORK = ["lift", "conduit", "slab", "trenching", "warehouse", "pedestal"]

# ---------------------------------------------------------------- services
# The three kinds of work on the trucks. Each gets a card and its own page.
SERVICES = [
    dict(key="industrial", page="industrial-electrician.html", title="Industrial", article="an",
         card="Plants, packing houses, cold storage and shops. We work around your production schedule and keep the line running.",
         items=["Motor controls, VFDs and starters", "480V three-phase power", "Switchgear and distribution panels",
                "Conduit and cable tray", "Machine and equipment hookups", "Troubleshooting and repair"],
         h1="Industrial Electrician <span>Santa Maria, CA</span>",
         seo_title="Industrial Electrician in Santa Maria, CA | Bendele Electric",
         desc="Industrial electrical contractor in Santa Maria, CA. Motor controls, 480V three-phase power, switchgear, conduit and equipment hookups. C-10 Lic. #881830. Call (805) 287-9044.",
         lede="Three-phase power, motor controls and equipment hookups for plants, packing houses, cold storage and shops in the Santa Maria Valley.",
         photo="warehouse",
         body=["A stopped line costs more than the repair does. We plan industrial work around your production schedule, show up with the material already on the truck, and stay until the equipment is running again.",
               "We install and service the power side of a plant: the gear that brings power in, the panels and conduit that carry it across the floor, and the starters and drives that run your motors. We also hook up new machines and chase down the faults that keep tripping the old ones.",
               "Every job is done under our California C-10 license, to code, with panels labeled so the next person who opens the door knows what they are looking at."],
         also=["New equipment and machine hookups", "Motor starters, VFDs and control wiring", "480V three-phase services and feeders",
               "Switchgear, panelboards and transformers", "Rigid conduit, EMT and cable tray", "Lighting for warehouses and yards",
               "Underground and trenching", "Troubleshooting, repair and shutdown work"]),
    dict(key="commercial", page="commercial-electrician.html", title="Commercial", article="a",
         card="Offices, retail, restaurants and tenant improvements, wired to code and finished on the date we gave you.",
         items=["Tenant and office build-outs", "Retail and parking lot lighting", "Exit and emergency lighting",
                "Data and network cabling", "Underground and trenching", "Preventive maintenance"],
         h1="Commercial Electrician <span>Santa Maria, CA</span>",
         seo_title="Commercial Electrician in Santa Maria, CA | Bendele Electric",
         desc="Commercial electrical contractor in Santa Maria, CA. Tenant improvements, office and retail build-outs, lighting, data cabling and underground. C-10 Lic. #881830. Call (805) 287-9044.",
         lede="Build-outs, lighting, underground and maintenance for offices, shops, restaurants and landlords across the Santa Maria Valley.",
         photo="conduit",
         body=["Commercial work runs on other people&rsquo;s deadlines: the lease start, the inspection, the opening day. We give you a date we can keep, coordinate with your general contractor and the other trades, and pass inspection the first time.",
               "We wire new spaces and tenant improvements from the service to the last receptacle, and we look after buildings that are already open: lighting that has gone dark, circuits that are overloaded, panels that have run out of room.",
               "Property managers and owners can call us for one-off repairs or for regular maintenance across several buildings."],
         also=["Tenant improvements and office build-outs", "Restaurant and retail wiring", "Interior, exterior and parking lot lighting",
               "Exit signs and emergency lighting", "Data and network cabling", "Service upgrades and new panels",
               "Underground conduit and trenching", "Preventive maintenance and repairs"]),
    dict(key="residential", page="residential-electrician.html", title="Residential", article="a",
         card="From a dead outlet to a whole new house. Clean work, fair prices, and we sweep up before we leave.",
         items=["Panel upgrades", "New construction and remodel wiring", "Outlets, switches and dimmers",
                "Indoor and outdoor lighting", "Ceiling fans", "Safety inspections"],
         h1="Residential Electrician <span>Santa Maria, CA</span>",
         seo_title="Residential Electrician in Santa Maria, CA | Bendele Electric",
         desc="Family-owned residential electrician in Santa Maria, CA. Panel upgrades, remodel and new construction wiring, lighting, outlets and repairs. C-10 Lic. #881830. Call (805) 287-9044.",
         lede="Repairs, upgrades and new wiring for homes in Santa Maria, Orcutt and the towns around them.",
         photo="truck",
         body=["Most house calls start the same way: something stopped working, or the house needs more power than it was built with. We find the cause, explain it in plain words, and give you a price before we start.",
               "We wire new homes and remodels, replace worn-out panels, add circuits for kitchens, shops and car chargers, and fix the outlets, switches and lights that have been bothering you for a year.",
               "We treat your house the way we would want ours treated. Drop cloths go down, boots stay clean, and the work area gets swept before we leave."],
         also=["Panel and service upgrades", "New construction and remodel wiring", "Outlets, switches, dimmers and GFCI protection",
               "Indoor, outdoor and landscape lighting", "Ceiling fans", "Dedicated circuits for appliances and shops",
               "EV charger circuits", "Troubleshooting and safety inspections"]),
]

# Specific jobs people search for by name.
JOBS = [
    dict(page="panel-upgrades.html", name="Panel upgrades", parent="residential",
         blurb="Replace an old or full breaker panel and get room to grow.",
         h1="Electrical Panel Upgrades <span>Santa Maria, CA</span>",
         seo_title="Electrical Panel Upgrades in Santa Maria, CA | Bendele Electric",
         desc="Electrical panel and service upgrades in Santa Maria, CA. Replace old fuse boxes and full breaker panels, with permit and inspection. C-10 Lic. #881830. Call (805) 287-9044.",
         lede="A new panel gives an older house or building the capacity and the protection it was never built with.",
         photo="fleet",
         body=["The panel is where every circuit in the building starts. When it is too small, too old or simply full, you see it as breakers that trip, lights that dim when the air conditioner starts, or no space left for the circuit you want to add.",
               "We replace fuse boxes and worn-out breaker panels, upgrade the service size when the building needs more power, and add subpanels for shops, additions and detached buildings. Before we quote, we look at what you run today and what you plan to add, so the new panel is sized for both.",
               "A panel change means the power is off for part of a day. We schedule the shutoff with the utility, pull the permit, and meet the inspector, so you are not left chasing paperwork."],
         also_title="Signs it is time",
         also=["Breakers trip often or will not reset", "The panel is warm, buzzing or shows rust or scorch marks",
               "It still uses screw-in fuses", "There are no open spaces for new circuits",
               "You are adding an EV charger, heat pump, spa or addition", "A home inspector or insurer flagged it"]),
    dict(page="ev-charger-installation.html", name="EV charger installation", parent="residential",
         blurb="A 240-volt circuit and charger for your garage, driveway or lot.",
         h1="EV Charger Installation <span>Santa Maria, CA</span>",
         seo_title="EV Charger Installation in Santa Maria, CA | Bendele Electric",
         desc="Home and workplace EV charger installation in Santa Maria, CA. 240V circuits, Level 2 chargers and panel capacity checks by a licensed C-10 electrician. Call (805) 287-9044.",
         lede="A dedicated 240-volt circuit, installed and inspected, so the car is full every morning.",
         photo="pedestal",
         body=["A Level 2 charger runs on a 240-volt circuit, the same kind that feeds a dryer or a range. It charges several times faster than the cord that plugs into a wall outlet, which is the difference between a full battery overnight and a partial one.",
               "We start by checking whether your panel has the capacity for the circuit. If it does, we run the wire, mount the charger or a 240-volt outlet where you park, and label the breaker. If it does not, we will tell you what it takes, whether that is a load-managing charger or a panel upgrade.",
               "We install the charger you already bought or wire for the one you plan to buy, at homes, shops and employee or customer parking."],
         also_title="What we take care of",
         also=["Panel capacity check before any work", "Dedicated 240V circuit and breaker", "Hardwired chargers or a 240V outlet",
               "Garage, carport, driveway and parking lot locations", "Trenching to detached garages and lots", "Permit and inspection"]),
]

# ---------------------------------------------------------------- service area
# Towns served besides Santa Maria itself (which is the home page).
AREAS = [
    dict(slug="orcutt", town="Orcutt", photo="lift",
         lede="Orcutt is next door to Santa Maria, which makes it some of the shortest drives we make.",
         body=["Orcutt has a bit of everything: older houses around Old Town, tract homes from the sixties through the eighties, and newer neighborhoods on the south end. The older homes are where we see panels that have run out of room and wiring that was never meant for today&rsquo;s loads.",
               "We also work for the shops, offices and restaurants along Clark Avenue and Bradley Road, from a single dead circuit to a full tenant improvement."],
         jobs=["Panel upgrades in older homes", "Remodel and addition wiring", "EV charger circuits",
               "Lighting and outlet repairs", "Tenant improvements for shops and offices"]),
    dict(slug="guadalupe", town="Guadalupe", photo="warehouse",
         lede="Guadalupe sits west of Santa Maria on Highway 1, in the middle of the valley&rsquo;s farm ground.",
         body=["A lot of the electrical work around Guadalupe is tied to produce: coolers, packing and shipping buildings, shops and yards. That means three-phase power, motors and controls, and jobs that have to fit around harvest.",
               "In town we work on homes old and new, and on the older commercial buildings along Guadalupe Street, where a new tenant often means new wiring."],
         jobs=["Three-phase power and motor controls", "Equipment hookups for coolers and packing lines",
               "Yard and building lighting", "Rewiring older commercial buildings", "Home repairs and panel upgrades"]),
    dict(slug="nipomo", town="Nipomo", photo="trenching",
         lede="Nipomo is a short run north on the 101, just over the San Luis Obispo County line.",
         body=["Much of Nipomo is spread across the Mesa on larger lots, so the work often reaches past the house: power out to a shop or barn, a well pump, a gate, or a long underground run to a detached building.",
               "Nipomo is unincorporated, so permits go through San Luis Obispo County. We pull the permit and meet the inspector as part of the job."],
         jobs=["Underground power to shops, barns and detached garages", "Well pump and gate circuits",
               "Panel and service upgrades", "New home and remodel wiring", "EV charger circuits"]),
    dict(slug="arroyo-grande", town="Arroyo Grande", photo="conduit",
         lede="Arroyo Grande and the rest of the Five Cities are an easy drive up the 101 from our base in Santa Maria.",
         body=["The Village has some of the oldest buildings on this part of the coast, and old buildings come with old wiring. We update services and panels, and rewire shops and restaurants when a space changes hands.",
               "Outside the Village we work on homes, offices and light industrial buildings throughout Arroyo Grande and the neighboring towns."],
         jobs=["Service and panel upgrades in older buildings", "Restaurant and retail wiring",
               "Home remodels and additions", "Lighting and outlet repairs", "Tenant improvements"]),
    dict(slug="los-alamos", town="Los Alamos", photo="truck",
         lede="Los Alamos is a quick trip south on the 101, a small town with a lot going on along Bell Street.",
         body=["The old buildings on Bell Street now hold tasting rooms, restaurants and inns, and each new use asks more of wiring that was put in generations ago. We bring those spaces up to what a kitchen or a tasting room needs.",
               "Around town are ranches and vineyards, where the work is power for barns, shops, pumps and outbuildings."],
         jobs=["Rewiring older commercial buildings", "Restaurant and tasting room wiring",
               "Power for barns, shops and pumps", "Home repairs and panel upgrades", "Outdoor and landscape lighting"]),
    dict(slug="lompoc", town="Lompoc", photo="slab",
         lede="Lompoc is southwest of Santa Maria, and we make the drive for homes, businesses and industrial buildings alike.",
         body=["Lompoc runs its own city electric utility, so a service upgrade here is coordinated with the City rather than with PG&amp;E. We handle that scheduling along with the permit.",
               "The work ranges from older homes that need a new panel to the warehouse spaces on the east side of town that have been turned into wineries and workshops, where tenants need three-phase power and equipment hookups."],
         jobs=["Panel and service upgrades", "Winery and workshop equipment hookups", "Three-phase power for warehouse spaces",
               "Home repairs and remodel wiring", "Commercial lighting"]),
    dict(slug="santa-ynez-valley", town="Santa Ynez Valley", short="the Santa Ynez Valley", photo="pedestal",
         lede="Buellton, Solvang, Santa Ynez, Los Olivos and Ballard are all within reach of our trucks.",
         body=["The valley is ranches, vineyards and horse properties, so power often has to travel: out to a barn, an arena, a well, a gate or a guest house. We trench and run underground feeders, and set subpanels where the power is needed.",
               "In the towns we work on homes, tasting rooms, restaurants and shops, from repairs to full build-outs."],
         jobs=["Underground feeders to barns and outbuildings", "Well pump, gate and arena power",
               "Winery and tasting room wiring", "Panel and service upgrades", "Home remodels and new construction"]),
]
for a in AREAS:
    a["page"] = f"electrician-{a['slug']}.html"
    a.setdefault("short", a["town"])
TOWNS = ["Santa Maria"] + [a["town"] for a in AREAS]
TOWNS_LINE = ", ".join(TOWNS[:-1]) + " and the " + TOWNS[-1]

TEAM = [("Anthony Bendele", "Founder"), ("Ryan Bendele", "Journeyman electrician"), ("David", "Electrician")]

STEPS = [
    ("Call or send the details", "Tell us what is going on. A few photos help."),
    ("We look and give you a price", "For most jobs we come out, see it in person, and write up a free estimate."),
    ("We do the work", "Permit pulled where one is required, material on the truck, and a date we keep."),
    ("Inspection and walkthrough", "We meet the inspector, show you what was done, and leave the place clean."),
]


# ---------------------------------------------------------------- helpers
def pic(name, sizes, eager=False, alt=None):
    w, h = PHOTOS[name]
    sw, sh = (800, 600) if w > h else (600, 800)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="assets/photos/{name}-800.jpg" srcset="assets/photos/{name}-800.jpg {sw}w, '
            f'assets/photos/{name}-1600.jpg {w}w" sizes="{sizes}" width="{sw}" height="{sh}" '
            f'alt="{alt or PHOTO_TEXT[name][1]}" {load}>')


def figure(name, cls, sizes, eager=False, extra="", caption=True):
    cap = f'\n    <figcaption>{PHOTO_TEXT[name][0]}</figcaption>' if caption else ""
    return f'<figure class="{cls}">\n    {extra}{pic(name, sizes, eager)}{cap}\n  </figure>'


def ld(data):
    return '<script type="application/ld+json">\n' + json.dumps(data, indent=2) + '\n</script>'


def business_schema():
    return {
        "@context": "https://schema.org", "@type": "Electrician", "@id": f"{SITE}/#business",
        "name": NAME, "url": f"{SITE}/",
        "image": f"{SITE}/assets/photos/truck-1600.jpg",
        "logo": f"{SITE}/assets/bendele-electric-logo.png",
        "telephone": PHONE, "faxNumber": FAX, "email": EMAIL,
        "description": f"Family-owned electrical contractor in Santa Maria, CA, in business for {YEARS} years. "
                       f"Industrial, commercial and residential electrical work. California C-10 License #{LICENSE}.",
        "address": {"@type": "PostalAddress", "postOfficeBoxNumber": "1845", "addressLocality": "Santa Maria",
                    "addressRegion": "CA", "postalCode": "93456", "addressCountry": "US"},
        "areaServed": [{"@type": "Place", "name": f"{t}, CA"} for t in TOWNS],
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification",
                                      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                      "opens": "07:00", "closes": "15:30"},
        "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "license",
                          "name": f"California C-10 Electrical Contractor License #{LICENSE}",
                          "recognizedBy": {"@type": "Organization", "name": "Contractors State License Board"}},
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Electrical services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"{s['title']} electrical services",
                                               "url": f"{SITE}/{s['page']}"}} for s in SERVICES]},
    }


def crumbs_schema(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE}/{p}"}
        for i, (n, p) in enumerate([("Home", "")] + trail)]}


def service_schema(name, page, area="Santa Maria, CA"):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "url": f"{SITE}/{page}",
            "serviceType": name, "areaServed": area, "provider": {"@id": f"{SITE}/#business"}}


def crumbs(trail):
    parts = ['<a href="index.html">Home</a>'] + [f'<a href="{p}">{n}</a>' for n, p in trail[:-1]] + [trail[-1][0]]
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<i aria-hidden="true">/</i>'.join(parts) + '</nav>'


NAV = [("Services", "services.html"), ("Service Area", "index.html#area"),
       ("About", "about.html"), ("Contact", "contact.html")]
PAGES = []   # (file, in sitemap, priority)


def page(file, title, desc, body, schemas=(), index=True, priority="0.6", current=None, scripts=""):
    canon = f"{SITE}/" if file == "index.html" else f"{SITE}/{file}"
    cur = ' aria-current="page"'
    nav = "\n".join(
        f'      <a href="{href}" class="nav__link"{cur if href == current else ""}>{label}</a>'
        for label, href in NAV)
    robots = "" if index else '<meta name="robots" content="noindex, follow">\n'
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/photos/truck-1600.jpg">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="{NAME}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff">
<link rel="apple-touch-icon" sizes="180x180" href="assets/favicon_io/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon_io/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon_io/favicon-16x16.png">
<link rel="shortcut icon" href="assets/favicon_io/favicon.ico">
<link rel="manifest" href="assets/favicon_io/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{FONTS}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css">
{scripts}{"".join(ld(s) + chr(10) for s in schemas)}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">
  <span class="topbar__lic">C-10 Lic. #{LICENSE}</span>
  <span class="topbar__hours">Mon&ndash;Fri 7:00&ndash;3:30</span>
  <a class="topbar__phone" href="tel:{TEL}">{PHONE}</a>
</div>
<header class="site-header">
  <nav class="nav" aria-label="Main">
    <a href="index.html" class="nav__logo"><img src="assets/bendele-electric-logo.svg" width="182" height="36" alt="{NAME}"></a>
    <button class="nav__mobile-toggle" type="button" aria-expanded="false" aria-label="Toggle navigation menu">
      <svg class="nav__mobile-icon" width="28" height="28" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
    </button>
    <div class="nav__menu">
{nav}
      <a href="tel:{TEL}" class="nav__link nav__phone">{PHONE}</a>
      <a href="quote.html" class="nav__cta">Get a Quote</a>
    </div>
  </nav>
</header>
<main id="main">
{body}</main>
<footer class="site-footer">
  <div class="site-footer__inner">
    <div class="site-footer__brand">
      <p class="site-footer__name">{NAME}</p>
      <p>Family-owned electrical contractor.<br>{YEARS} years in business.<br>Industrial &middot; Commercial &middot; Residential</p>
      <p>California C-10 License #{LICENSE}<br>Licensed, bonded and insured</p>
    </div>
    <address class="site-footer__contact">
      <h2>Contact</h2>
      <p><a href="tel:{TEL}">{PHONE}</a><br>Fax {FAX}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>P.O. Box 1845<br>Santa Maria, CA 93456</p>
      <p>{HOURS}</p>
    </address>
    <nav class="site-footer__nav" aria-label="Services">
      <h2>Services</h2>
      <ul>
{chr(10).join(f'        <li><a href="{s["page"]}">{s["title"]}</a></li>' for s in SERVICES)}
{chr(10).join(f'        <li><a href="{j["page"]}">{j["name"]}</a></li>' for j in JOBS)}
        <li><a href="quote.html">Get a quote</a></li>
      </ul>
    </nav>
    <nav class="site-footer__nav" aria-label="Service area">
      <h2>Service area</h2>
      <ul>
        <li><a href="index.html">Santa Maria</a></li>
{chr(10).join(f'        <li><a href="{a["page"]}">{a["town"]}</a></li>' for a in AREAS)}
      </ul>
    </nav>
  </div>
  <div class="site-footer__legal">
    <span>&copy; {date.today().year} {NAME}</span>
    <a href="privacy-policy.html">Privacy Policy</a>
    <a href="terms-of-service.html">Terms of Service</a>
  </div>
</footer>
<div class="callbar">
  <a class="callbar__call" href="tel:{TEL}">Call {PHONE}</a>
  <a class="callbar__quote" href="quote.html">Get a Quote</a>
</div>
<script src="nav.js" defer></script>
</body>
</html>
"""
    (ROOT / file).write_text(html)
    PAGES.append((file, index, priority))


def head(kicker, h1, lede, trail=None, actions=True):
    act = f"""  <div class="hero__actions">
    <a class="btn btn--call" href="tel:{TEL}"><span class="btn__label">Call</span> {PHONE}</a>
    <a class="btn btn--quote" href="quote.html">Get a free quote</a>
  </div>
""" if actions else ""
    return f"""<section class="page-head">
  {crumbs(trail) if trail else ""}
  <p class="hero__kicker">{kicker}</p>
  <h1 class="hero__title">{h1}</h1>
  <p class="hero__lede">{lede}</p>
{act}</section>
"""


def section_head(num, title, intro=""):
    intro = f'\n    <p class="section__intro">{intro}</p>' if intro else ""
    return f"""  <header class="section__head">
    <p class="section__num">{num}</p>
    <h2 class="section__title">{title}</h2>{intro}
  </header>"""


def cta(title="Tell us what you need wired.",
        text="Call during shop hours, or send the details and we will get back to you with a free estimate."):
    return f"""<section class="cta">
  <h2 class="cta__title">{title}</h2>
  <p class="cta__text">{text}</p>
  <a class="cta__phone" href="tel:{TEL}">{PHONE}</a>
  <a class="btn btn--quote" href="quote.html">Get a free quote</a>
</section>
"""


def service_cards(more=True):
    out = []
    for i, s in enumerate(SERVICES, 1):
        link = (f'\n      <a class="service__more" href="{s["page"]}">More about {s["key"]} work</a>' if more else "")
        out.append(f'''    <article class="service" id="{s["key"]}" data-n="0{i}">
      <h3 class="service__title">{s["title"]}</h3>
      <p class="service__text">{s["card"]}</p>
      <ul class="service__list">{"".join(f"<li>{x}</li>" for x in s["items"])}</ul>{link}
      <a class="service__link" href="quote.html?type={s["key"]}">Get {s["article"]} {s["key"]} quote</a>
    </article>''')
    return "\n".join(out)


def steps():
    items = "\n".join(f"    <li><h3>{t}</h3><p>{p}</p></li>" for t, p in STEPS)
    return f'  <ol class="steps">\n{items}\n  </ol>'


def area_list():
    items = ["    <li>Santa Maria</li>"] + [f'    <li><a href="{a["page"]}">{a["town"]}</a></li>' for a in AREAS]
    return '  <ul class="area__list">\n' + "\n".join(items) + "\n  </ul>"


def service_links(exclude=None):
    return ('  <div class="jobs jobs--3">\n' + "\n".join(
        f'    <a href="{s["page"]}"><b>{s["title"]}</b><span>{s["lede"]}</span></a>'
        for s in SERVICES if s is not exclude) + "\n  </div>")


def jobs_grid():
    return ('  <div class="jobs">\n' + "\n".join(
        f'    <a href="{j["page"]}"><b>{j["name"]}</b><span>{j["blurb"]}</span></a>' for j in JOBS) + "\n  </div>")


# ---------------------------------------------------------------- pages
def build_home():
    stamp = '<p class="hero__stamp"><b>' + YEARS + '</b> <span>Years in</span> <span>Business</span></p>\n    '
    work = "\n".join(
        f'''    <figure class="work__item">
      {pic(n, "(min-width: 900px) 33vw, (min-width: 600px) 50vw, 100vw")}
      <figcaption>{PHOTO_TEXT[n][0]}</figcaption>
    </figure>''' for n in WORK)
    body = f"""<section class="hero">
  <div class="hero__text">
    <p class="hero__kicker">Need an electrician?</p>
    <h1 class="hero__title">Santa Maria&rsquo;s <span>Family Electrician</span></h1>
    <p class="hero__lede">Bendele Electric is a family-owned shop. We wire, repair and upgrade electrical systems for plants, businesses and homes across the Santa Maria Valley, and the people who quote your job are the people who show up to do it.</p>
    <div class="hero__actions">
      <a class="btn btn--call" href="tel:{TEL}"><span class="btn__label">Call</span> {PHONE}</a>
      <a class="btn btn--quote" href="quote.html">Get a free quote</a>
    </div>
  </div>
  {figure("truck", "hero__media", "(min-width: 900px) 55vw, 100vw", eager=True, extra=stamp)}
</section>

<section id="services" class="section services">
{section_head("01", "What we do", "Three kinds of work, the same crew on all of them.")}
  <div class="services__grid">
{service_cards()}
  </div>
</section>

<section id="work" class="section work">
{section_head("02", "Recent work")}
  <div class="work__grid">
{work}
  </div>
</section>

<section id="area" class="section area">
{section_head("03", "Where we work", "Based in Santa Maria and on the road across northern Santa Barbara County and the Five Cities.")}
{area_list()}
  <p class="area__note">Not on the list? Call and ask. If we can drive there, we can probably wire it.</p>
</section>

<section id="about" class="section about">
{section_head("04", "About the shop")}
  <div class="about__body">
    <div class="about__text">
      <p>Anthony Bendele started Bendele Electric twenty years ago, and it is still a family business. That means no call center, no salesman and no handing your job to whoever is free.</p>
      <p>We do the work the way we would want it done at our own place: pulled permits, straight conduit, labeled panels and a clean site at the end of the day.</p>
      <dl class="about__facts">
        <div><dt>License</dt><dd>California C-10 #{LICENSE}</dd></div>
        <div><dt>Coverage</dt><dd>Bonded and insured</dd></div>
        <div><dt>In business</dt><dd>{YEARS} years</dd></div>
        <div><dt>Hours</dt><dd>Mon&ndash;Fri, 7:00&ndash;3:30</dd></div>
      </dl>
      <a class="about__more" href="about.html">More about Bendele Electric</a>
    </div>
    {figure("fleet", "about__media", "(min-width: 900px) 45vw, 100vw")}
  </div>
</section>

{cta()}"""
    page("index.html", "Electrician in Santa Maria, CA | Bendele Electric Inc. | Lic. #881830",
         f"Family-owned electrical contractor in Santa Maria, CA, {YEARS} years in business. Industrial, commercial "
         f"and residential electricians. C-10 Lic. #{LICENSE}. Call {PHONE}.",
         body, schemas=[business_schema()], priority="1.0")


def build_services():
    body = head("What we do", "Electrical Services <span>Santa Maria, CA</span>",
                "Industrial, commercial and residential electrical work from one family-owned shop. Pick the kind of work below, or call and tell us what you need.",
                trail=[("Services", "services.html")]) + f"""
<section class="section">
{section_head("01", "Three kinds of work")}
{service_links()}
</section>

<section class="section">
{section_head("02", "Common jobs", "Two of the jobs we are asked about most.")}
{jobs_grid()}
</section>

<section class="section">
{section_head("03", "How a job goes")}
{steps()}
</section>

{cta()}"""
    page("services.html", "Electrical Services in Santa Maria, CA | Bendele Electric",
         f"Industrial, commercial and residential electrical services in Santa Maria, CA: panel upgrades, EV chargers, "
         f"tenant improvements, motor controls and repairs. C-10 Lic. #{LICENSE}.",
         body, schemas=[crumbs_schema([("Services", "services.html")])], priority="0.9", current="services.html")


def detail_page(d, kicker, list_title, trail, quote_type, name, related_html, priority):
    paras = "\n".join(f"      <p>{p}</p>" for p in d["body"])
    ticks = "".join(f"<li>{x}</li>" for x in d["also"])
    body = head(kicker, d["h1"], d["lede"], trail=trail) + f"""
<section class="section">
  <div class="split">
    <div class="prose">
{paras}
      <h2>{list_title}</h2>
      <ul class="ticks">{ticks}</ul>
    </div>
    {figure(d["photo"], "split__media", "(min-width: 900px) 40vw, 100vw", caption=False)}
  </div>
</section>

<section class="section">
{section_head("01", "How a job goes")}
{steps()}
</section>

{related_html}
{cta(text=f'Call during shop hours, or <a href="quote.html?type={quote_type}">send the details</a> and we will get back to you with a free estimate.')}"""
    page(d["page"], d["seo_title"], d["desc"], body,
         schemas=[service_schema(name, d["page"]), crumbs_schema(trail)], priority=priority, current="services.html")


def build_service_pages():
    for s in SERVICES:
        others = [o for o in SERVICES if o is not s]
        links = [f'    <a href="{j["page"]}"><b>{j["name"]}</b><span>{j["blurb"]}</span></a>'
                 for j in JOBS if j["parent"] == s["key"]]
        links += [f'    <a href="{o["page"]}"><b>{o["title"]} work</b><span>{o["lede"]}</span></a>' for o in others]
        related = f"""<section class="section">
{section_head("02", "Related work")}
  <div class="jobs">
{chr(10).join(links)}
  </div>
</section>
"""
        detail_page(s, f"{s['title']} electrical", "What we take on",
                    [("Services", "services.html"), (s["title"], s["page"])], s["key"],
                    f"{s['title']} electrical services", related, "0.8")
    for j in JOBS:
        parent = next(s for s in SERVICES if s["key"] == j["parent"])
        other = [o for o in JOBS if o is not j]
        links = [f'    <a href="{o["page"]}"><b>{o["name"]}</b><span>{o["blurb"]}</span></a>' for o in other]
        links.append(f'    <a href="{parent["page"]}"><b>{parent["title"]} work</b><span>{parent["lede"]}</span></a>')
        related = f"""<section class="section">
{section_head("02", "Related work")}
  <div class="jobs">
{chr(10).join(links)}
  </div>
</section>
"""
        detail_page(j, "Licensed and permitted", j["also_title"],
                    [("Services", "services.html"), (j["name"], j["page"])], j["parent"],
                    j["name"], related, "0.8")


def build_area_pages():
    for a in AREAS:
        town, short = a["town"], a["short"]
        trail = [("Service Area", "index.html#area"), (town, a["page"])]
        paras = "\n".join(f"      <p>{p}</p>" for p in a["body"])
        ticks = "".join(f"<li>{x}</li>" for x in a["jobs"])
        body = head("We work here", f"Electrician in <span>{town}, CA</span>", a["lede"], trail=trail) + f"""
<section class="section">
  <div class="split">
    <div class="prose">
{paras}
      <h2>Common jobs in {short}</h2>
      <ul class="ticks">{ticks}</ul>
    </div>
    {figure(a["photo"], "split__media", "(min-width: 900px) 40vw, 100vw", caption=False)}
  </div>
</section>

<section class="section">
{section_head("01", "What we do", f"Industrial, commercial and residential work in {short}.")}
{service_links()}
</section>

{cta(title=f"Need an electrician in {short}?")}"""
        page(a["page"], f"Electrician in {town}, CA | Bendele Electric Inc.",
             f"Family-owned electrician serving {short}, CA from Santa Maria. Industrial, commercial and residential "
             f"electrical work. C-10 Lic. #{LICENSE}. Call {PHONE}.",
             body, schemas=[service_schema(f"Electrician in {town}, CA", a["page"], f"{town}, CA"),
                            crumbs_schema([(town, a["page"])])], priority="0.7")


def build_about():
    team = "\n".join(f'    <li><p class="team__name">{n}</p><p class="team__role">{r}</p></li>' for n, r in TEAM)
    body = head("Family owned", f"About <span>Bendele Electric</span>",
                f"A family-owned electrical contractor in Santa Maria, California, {YEARS} years in business.",
                trail=[("About", "about.html")], actions=False) + f"""
<section class="section">
    <div class="prose">
      <h2>Our story</h2>
      <p>Anthony Bendele started Bendele Electric twenty years ago with a truck, a license and a simple idea: do the job right, charge a fair price, and answer the phone. It is still a family business, and it still runs that way.</p>
      <p>Over the years the work has grown from house calls to plants, packing houses and commercial buildings across the Santa Maria Valley. We still do all three, and we bring the same habits to each.</p>
      <h2>How we work</h2>
      <ul>
        <li><strong>A price before we start.</strong> Free estimates, in writing, with no surprises on the invoice.</li>
        <li><strong>Dates we keep.</strong> If we tell you Tuesday, we mean Tuesday.</li>
      </ul>
    </div>
</section>

<section class="section">
{section_head("01", "Who you will meet")}
  <ul class="team">
{team}
  </ul>
</section>

{cta(title="Ready to work with us?")}"""
    page("about.html", "About Bendele Electric | Family-Owned Santa Maria Electrician",
         f"Bendele Electric is a family-owned electrical contractor in Santa Maria, CA, in business for {YEARS} years. "
         f"California C-10 License #{LICENSE}.",
         body, schemas=[crumbs_schema([("About", "about.html")])], priority="0.7", current="about.html")


def build_contact():
    body = head("Get in touch", "Contact <span>Bendele Electric</span>",
                "Calling is the fastest way to reach us during shop hours. For a price on a job, the quote form gets us the details we need.",
                trail=[("Contact", "contact.html")], actions=False) + f"""
<section class="section">
  <div class="boxes">
    <article class="box">
      <h2 class="box__title">Phone</h2>
      <div class="box__body">
        <a class="box__big" href="tel:{TEL}">{PHONE}</a>
        <p>Fax {FAX}</p>
      </div>
    </article>
    <article class="box">
      <h2 class="box__title">Email</h2>
      <div class="box__body">
        <a class="box__big box__big--small" href="mailto:{EMAIL}">{EMAIL}</a>
        <p>For estimates, the <a href="quote.html">quote form</a> is quicker.</p>
      </div>
    </article>
    <article class="box">
      <h2 class="box__title">Hours</h2>
      <div class="box__body">
        <p><strong>Monday to Friday</strong><br>7:00 AM to 3:30 PM</p>
        <p><strong>Saturday and Sunday</strong><br>Closed</p>
      </div>
    </article>
    <article class="box">
      <h2 class="box__title">Mailing address</h2>
      <div class="box__body">
        <address><p>{NAME}<br>P.O. Box 1845<br>Santa Maria, CA 93456</p></address>
        <p>We come to you, so there is no storefront to visit.</p>
        <p>California C-10 License #{LICENSE}</p>
      </div>
    </article>
  </div>
</section>

{cta(title="Need a price on a job?", text="Send the details and we will get back to you with a free estimate.")}"""
    page("contact.html", f"Contact Bendele Electric | {PHONE} | Santa Maria, CA",
         f"Call Bendele Electric at {PHONE} or email {EMAIL}. Family-owned electrician in Santa Maria, CA. "
         f"Open Monday to Friday, 7:00 AM to 3:30 PM.",
         body, schemas=[crumbs_schema([("Contact", "contact.html")])], priority="0.8", current="contact.html")


def build_quote():
    form = (ROOT / "content/quote-form.html").read_text()
    body = f"""<section class="page-head">
  <p class="hero__kicker">Free estimates</p>
  <h1 class="hero__title">Request a quote</h1>
  <p class="hero__lede">Tell us about the job. The more detail you give, the closer our first number will be. Rather talk? Call <a href="tel:{TEL}">{PHONE}</a>, Monday to Friday, 7:00 to 3:30.</p>
</section>
{form}"""
    page("quote.html", "Free Electrical Quote in Santa Maria, CA | Bendele Electric Inc.",
         f"Request a free estimate from Bendele Electric, a family-owned electrical contractor in Santa Maria, CA. "
         f"Industrial, commercial and residential. Call {PHONE}.",
         body, priority="0.9",
         scripts='<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>\n'
                 '<script src="quote.js" defer></script>\n')


def build_legal():
    for file, title in [("privacy-policy.html", "Privacy Policy"), ("terms-of-service.html", "Terms of Service")]:
        text = (ROOT / "content" / file).read_text()
        body = f"""<section class="page-head">
  <p class="hero__kicker">Last updated December 4, 2025</p>
  <h1 class="hero__title">{title}</h1>
</section>
<section class="section">
  <div class="prose">
{text}  </div>
</section>
"""
        page(file, f"{title} | Bendele Electric", f"Bendele Electric's {title.lower()} for this website.",
             body, index=False)


def build_404():
    body = head("Wrong turn", "Page not found",
                "That page has moved or never existed. The links below will get you back on the road.", actions=False) + f"""
<section class="section">
  <div class="jobs">
    <a href="index.html"><b>Home</b><span>Start over from the front page.</span></a>
    <a href="services.html"><b>Services</b><span>Industrial, commercial and residential work.</span></a>
    <a href="quote.html"><b>Get a quote</b><span>Send the details for a free estimate.</span></a>
    <a href="contact.html"><b>Contact</b><span>Phone, email and hours.</span></a>
  </div>
</section>
"""
    page("404.html", "Page Not Found | Bendele Electric", "This page could not be found.", body, index=False)


def build_sitemap():
    today = date.today().isoformat()
    urls = "\n".join(
        f"    <url>\n        <loc>{SITE}/{'' if f == 'index.html' else f}</loc>\n        <lastmod>{today}</lastmod>\n"
        f"        <priority>{p}</priority>\n    </url>" for f, idx, p in PAGES if idx)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls + "\n</urlset>\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    build_home()
    build_services()
    build_service_pages()
    build_area_pages()
    build_about()
    build_contact()
    build_quote()
    build_legal()
    build_404()
    build_sitemap()
    print(f"built {len(PAGES)} pages")
