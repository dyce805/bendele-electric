#!/usr/bin/env python3
"""Generates the five design previews (home + quote page each).

Every design shares the same content and markup; only the fonts, a few
headline strings and style.css differ. Run:  python3 designs/build.py
"""
import json
from pathlib import Path
from string import Template

HERE = Path(__file__).parent
SITE = "https://bendele-electric.com"   # change here when the domain is decided
PHONE = "(805) 287-9044"
TEL = "+18052879044"
EMAIL = "info@bendeleelectric.com"
LICENSE = "881830"
TOWNS = ["Santa Maria", "Orcutt", "Guadalupe", "Nipomo", "Arroyo Grande",
         "Los Alamos", "Lompoc", "Santa Ynez Valley"]

# The chosen design. Its style.css holds structure only; colours come from a palette.css.
TRADE_AD = dict(fonts="family=Barlow+Condensed:wght@600;800&family=Barlow:wght@400;600",
                kicker="Need an electrician?",
                h1="Santa Maria&rsquo;s <span>Family Electrician</span>")

DESIGNS = [
    dict(slug="1-truck-door", name="Truck Door",
         fonts="family=Marcellus&family=Source+Sans+3:wght@400;600;700",
         kicker="Industrial &middot; Commercial &middot; Residential",
         h1="Electrical Contractor <span>Santa Maria, California</span>"),
    dict(slug="2-panel-schedule", name="Panel Schedule",
         fonts="family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Condensed:wght@400;600;700",
         kicker="Sheet E-1 &nbsp;/&nbsp; Bendele Electric Inc.",
         h1="Electrician <span>Santa Maria, CA</span>"),
    dict(slug="3-central-coast", name="Central Coast",
         fonts="family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Karla:wght@400;600",
         kicker="Family-owned on the Central Coast",
         h1="Your Santa Maria Valley electrician, <span>for over twenty years.</span>"),
    dict(slug="4-trade-ad", name="Trade Ad", theme="#c9cdd2",
         css=["style.css", "../4a-brushed-silver/palette.css"], **TRADE_AD),
    dict(slug="5-plain-spoken", name="Plain Spoken",
         fonts="family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&family=Schibsted+Grotesk:wght@400;600",
         kicker="Bendele Electric Inc.",
         h1="A family-owned electrician in <span>Santa Maria, California.</span>"),
]

# Colour options for the Trade Ad. Each folder holds a hand-written palette.css.
PALETTES = [("4a-brushed-silver", "Brushed Silver", "#c9cdd2"),
            ("4b-black-chrome", "Black Chrome", "#141414"),
            ("4c-green-field", "Green Field", "#2f7a36"),
            ("4d-white-truck", "White Truck", "#ffffff")]
DESIGNS += [dict(slug=slug, name=name, theme=theme,
                 css=["../4-trade-ad/style.css", "palette.css"], **TRADE_AD)
            for slug, name, theme in PALETTES]

# name: (width, height) of the large file; the small one is half of 1600
PHOTOS = {
    "truck": (1170, 878), "fleet": (1600, 1200), "lift": (1600, 1200), "slab": (1600, 1200),
    "conduit": (1200, 1600), "warehouse": (1200, 1600), "trenching": (1200, 1600),
    "pedestal": (1200, 1600),
}


def pic(name, alt, sizes, eager=False):
    w, h = PHOTOS[name]
    sw, sh = (800, 600) if w > h else (600, 800)
    base = f"../../assets/photos/{name}"
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="{base}-800.jpg" srcset="{base}-800.jpg {sw}w, {base}-1600.jpg {w}w" '
            f'sizes="{sizes}" width="{sw}" height="{sh}" alt="{alt}" {load}>')


SERVICES = [
    ("01", "industrial", "Industrial",
     "Plants, packing houses, cold storage and shops. We work around your production schedule and keep the line running.",
     ["Motor controls, VFDs and starters", "480V three-phase power", "Switchgear and distribution panels",
      "Conduit and cable tray", "Machine and equipment hookups", "Troubleshooting and repair"]),
    ("02", "commercial", "Commercial",
     "Offices, retail, restaurants and tenant improvements, wired to code and finished on the date we gave you.",
     ["Tenant and office build-outs", "Retail and parking lot lighting", "Exit and emergency lighting",
      "Data and network cabling", "Underground and trenching", "Preventive maintenance"]),
    ("03", "residential", "Residential",
     "From a dead outlet to a whole new house. Clean work, fair prices, and we sweep up before we leave.",
     ["Panel upgrades", "New construction and remodel wiring", "Outlets, switches and dimmers",
      "Indoor and outdoor lighting", "Ceiling fans", "Safety inspections"]),
]

WORK = [
    ("lift", "Running conduit to a warehouse electrical room.",
     "Bendele Electric electrician on a scissor lift bending conduit outside a warehouse electrical room"),
    ("conduit", "Racked conduit runs in a commercial building.",
     "Electrician on a scissor lift installing racked conduit runs along a block wall"),
    ("slab", "Underground conduit stubbed up before a slab pour.",
     "Underground electrical conduit stubbed up through rebar before a concrete slab pour"),
    ("trenching", "Trenching a parking lot for new underground power.",
     "Bendele Electric crew member trenching across a parking lot for underground conduit"),
    ("warehouse", "Equipment hookup on a warehouse floor.",
     "Bendele Electric electrician wiring equipment on a warehouse floor"),
    ("pedestal", "New power pedestal with 50 and 30 amp outlets.",
     "Newly installed outdoor power pedestal with 50 amp and 30 amp receptacles"),
]

HEAD = Template("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<meta name="description" content="$desc">
<meta name="robots" content="noindex">
<link rel="canonical" href="$site/$page">
<meta property="og:title" content="$title">
<meta property="og:description" content="$desc">
<meta property="og:type" content="website">
<meta property="og:url" content="$site/$page">
<meta property="og:image" content="$site/assets/photos/truck-1600.jpg">
<meta property="og:locale" content="en_US">
<meta property="og:site_name" content="Bendele Electric Inc.">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="$theme">
<link rel="apple-touch-icon" sizes="180x180" href="../../assets/favicon_io/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="../../assets/favicon_io/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="../../assets/favicon_io/favicon-16x16.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?$fonts&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../shared/base.css">
$styles
$extra_head
</head>
<body class="page-$kind">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">
  <span class="topbar__lic">C-10 Lic. #$license</span>
  <span class="topbar__hours">Mon&ndash;Fri 7:00&ndash;3:30</span>
  <a class="topbar__phone" href="tel:$tel">$phone</a>
</div>
<header class="site-header">
  <nav class="nav" aria-label="Main">
    <a href="index.html" class="nav__logo"><img src="../../assets/bendele-electric-logo.png" width="200" height="50" alt="Bendele Electric Inc."></a>
    <button class="nav__mobile-toggle" type="button" aria-expanded="false" aria-label="Toggle navigation menu">
      <svg class="nav__mobile-icon" width="28" height="28" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
    </button>
    <div class="nav__menu">
      <a href="${home}#services" class="nav__link">Services</a>
      <a href="${home}#work" class="nav__link">Our Work</a>
      <a href="${home}#area" class="nav__link">Service Area</a>
      <a href="${home}#about" class="nav__link">About</a>
      <a href="tel:$tel" class="nav__link nav__phone">$phone</a>
      <a href="quote.html" class="nav__cta">Get a Quote</a>
    </div>
  </nav>
</header>
<main id="main">
""")

FOOT = Template("""</main>
<footer class="site-footer">
  <div class="site-footer__inner">
    <div class="site-footer__brand">
      <p class="site-footer__name">Bendele Electric Inc.</p>
      <p>Family-owned electrical contractor.<br>20 years in business.<br>Industrial &middot; Commercial &middot; Residential</p>
      <p>California C-10 License #$license<br>Licensed, bonded and insured</p>
    </div>
    <address class="site-footer__contact">
      <p><a href="tel:$tel">$phone</a><br>Fax (805) 764-8636</p>
      <p><a href="mailto:$email">$email</a></p>
      <p>P.O. Box 1845<br>Santa Maria, CA 93456</p>
      <p>Mon&ndash;Fri 7:00 AM&ndash;3:30 PM</p>
    </address>
    <p class="site-footer__area">Serving $towns_line.</p>
  </div>
  <div class="site-footer__legal">
    <span>&copy; 2026 Bendele Electric Inc.</span>
    <a href="../../privacy-policy.html">Privacy Policy</a>
    <a href="../../terms-of-service.html">Terms of Service</a>
    <a href="../index.html">All designs</a>
  </div>
</footer>
<div class="callbar">
  <a class="callbar__call" href="tel:$tel">Call $phone</a>
  <a class="callbar__quote" href="quote.html">Get a Quote</a>
</div>
<script src="../../nav.js" defer></script>
</body>
</html>
""")

HOME = Template("""<section class="hero">
  <div class="hero__text">
    <p class="hero__kicker">$kicker</p>
    <h1 class="hero__title">$h1</h1>
    <p class="hero__lede">Bendele Electric is a three-person, family-owned shop. We wire, repair and upgrade electrical systems for plants, businesses and homes across the Santa Maria Valley, and the people who quote your job are the people who show up to do it.</p>
    <div class="hero__actions">
      <a class="btn btn--call" href="tel:$tel"><span class="btn__label">Call</span> $phone</a>
      <a class="btn btn--quote" href="quote.html">Get a free quote</a>
    </div>
    <ul class="hero__facts">
      <li><span>In business</span> 20 years</li>
      <li><span>License</span> C-10 #$license</li>
      <li><span>Owned by</span> The Bendele family</li>
      <li><span>Hours</span> Mon&ndash;Fri 7:00&ndash;3:30</li>
    </ul>
  </div>
  <figure class="hero__media">
    <p class="hero__stamp"><b>20</b> <span>Years in</span> <span>Business</span></p>
    $hero_img
    <figcaption>One of our service trucks hauling the lift to a job.</figcaption>
  </figure>
</section>

<section id="services" class="section services">
  <header class="section__head">
    <p class="section__num">01</p>
    <h2 class="section__title">What we do</h2>
    <p class="section__intro">Three kinds of work, the same crew on all of them.</p>
  </header>
  <div class="services__grid">
$services
  </div>
</section>

<section id="work" class="section work">
  <header class="section__head">
    <p class="section__num">02</p>
    <h2 class="section__title">Recent work</h2>
    <p class="section__intro">Our jobs, our photos. Nothing here is stock.</p>
  </header>
  <div class="work__grid">
$work
  </div>
</section>

<section id="area" class="section area">
  <header class="section__head">
    <p class="section__num">03</p>
    <h2 class="section__title">Where we work</h2>
    <p class="section__intro">Based in Santa Maria and on the road across northern Santa Barbara County and the Five Cities.</p>
  </header>
  <ul class="area__list">
$towns
  </ul>
  <p class="area__note">Not on the list? Call and ask. If we can drive there, we can probably wire it.</p>
</section>

<section id="about" class="section about">
  <header class="section__head">
    <p class="section__num">04</p>
    <h2 class="section__title">About the shop</h2>
  </header>
  <div class="about__body">
    <div class="about__text">
      <p>Anthony Bendele started Bendele Electric twenty years ago, and it is still a family business. There are three of us. That means no call center, no salesman and no handing your job to whoever is free.</p>
      <p>We do the work the way we would want it done at our own place: pulled permits, straight conduit, labeled panels and a clean site at the end of the day.</p>
      <dl class="about__facts">
        <div><dt>License</dt><dd>California C-10 #$license</dd></div>
        <div><dt>Coverage</dt><dd>Bonded and insured</dd></div>
        <div><dt>Crew</dt><dd>Three electricians</dd></div>
        <div><dt>In business</dt><dd>20 years</dd></div>
      </dl>
    </div>
    <figure class="about__media">
      $fleet_img
      <figcaption>Both trucks on a job site.</figcaption>
    </figure>
  </div>
</section>

<section class="cta">
  <h2 class="cta__title">Tell us what you need wired.</h2>
  <p class="cta__text">Call during shop hours, or send the details and we will get back to you with a free estimate.</p>
  <a class="cta__phone" href="tel:$tel">$phone</a>
  <a class="btn btn--quote" href="quote.html">Get a free quote</a>
</section>
""")

QUOTE = Template("""<section class="quote-head">
  <p class="hero__kicker">Free estimates</p>
  <h1 class="hero__title">Request a quote</h1>
  <p class="hero__lede">Tell us about the job. The more detail you give, the closer our first number will be. Rather talk? Call <a href="tel:$tel">$phone</a>, Monday to Friday, 7:00 to 3:30.</p>
</section>
<section class="quote-section">
  <form class="quote-form" id="quoteForm" novalidate>
    <fieldset class="form-set">
      <legend class="form-set__legend">Your details</legend>
      <div class="form-row">
        <div class="form-group">
          <label for="name" class="form-label">Full name <span class="form-required">*</span></label>
          <input type="text" id="name" name="name" class="form-input" autocomplete="name" required>
        </div>
        <div class="form-group">
          <label for="phone" class="form-label">Phone number <span class="form-required">*</span></label>
          <input type="tel" id="phone" name="phone" class="form-input" autocomplete="tel" inputmode="tel" placeholder="(805) 555-0123" required>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label for="email" class="form-label">Email address <span class="form-required">*</span></label>
          <input type="email" id="email" name="email" class="form-input" autocomplete="email" inputmode="email" required>
        </div>
        <div class="form-group">
          <label for="contactMethod" class="form-label">Best way to reach you</label>
          <select id="contactMethod" name="contactMethod" class="form-select">
            <option value="phone">Phone call</option>
            <option value="email">Email</option>
            <option value="text">Text message</option>
          </select>
        </div>
      </div>
    </fieldset>

    <fieldset class="form-set">
      <legend class="form-set__legend">The property</legend>
      <div class="form-group">
        <label for="serviceAddress" class="form-label">Service address <span class="form-required">*</span></label>
        <input type="text" id="serviceAddress" name="serviceAddress" class="form-input" autocomplete="street-address" placeholder="123 Broadway, Santa Maria, CA 93454" required>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label for="propertyType" class="form-label">Property type <span class="form-required">*</span></label>
          <select id="propertyType" name="propertyType" class="form-select" required>
            <option value="" disabled selected>Select one</option>
            <option value="residential">Residential</option>
            <option value="commercial">Commercial</option>
            <option value="industrial">Industrial</option>
            <option value="agricultural">Agricultural</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div class="form-group" id="otherPropertyGroup" style="display: none;">
          <label for="otherProperty" class="form-label">Describe the property <span class="form-required">*</span></label>
          <input type="text" id="otherProperty" name="otherProperty" class="form-input" placeholder="Church, school, winery...">
        </div>
      </div>
    </fieldset>

    <fieldset class="form-set">
      <legend class="form-set__legend">The job</legend>
      <div class="form-group">
        <label for="workType" class="form-label">Type of work needed <span class="form-required">*</span></label>
        <input type="text" id="workType" name="workType" class="form-input" placeholder="Panel upgrade, new circuit, lighting repair..." required>
      </div>
      <div class="form-group">
        <label for="projectDescription" class="form-label">Project description</label>
        <textarea id="projectDescription" name="projectDescription" class="form-textarea" rows="4" placeholder="What is going on, what you want done, anything we should know before we come out."></textarea>
      </div>
      <div class="form-row">
        <div class="form-group">
          <label for="urgency" class="form-label">How soon?</label>
          <select id="urgency" name="urgency" class="form-select">
            <option value="flexible">Flexible, no rush</option>
            <option value="routine">Within a few weeks</option>
            <option value="soon">Within a week</option>
            <option value="urgent">As soon as possible</option>
            <option value="emergency">Emergency</option>
          </select>
        </div>
        <div class="form-group">
          <label for="completionDate" class="form-label">Needed by</label>
          <input type="date" id="completionDate" name="completionDate" class="form-input">
        </div>
      </div>
    </fieldset>

    <fieldset class="form-set">
      <legend class="form-set__legend">Anything else</legend>
      <div class="form-group">
        <label for="howHeard" class="form-label">How did you hear about us?</label>
        <select id="howHeard" name="howHeard" class="form-select">
          <option value="" disabled selected>Select one</option>
          <option value="google">Google search</option>
          <option value="referral">Friend or family</option>
          <option value="socialMedia">Social media</option>
          <option value="driveBy">Saw one of our trucks</option>
          <option value="repeat">Returning customer</option>
          <option value="other">Other</option>
        </select>
      </div>
      <div class="form-group">
        <label for="additionalComments" class="form-label">Additional comments</label>
        <textarea id="additionalComments" name="additionalComments" class="form-textarea" rows="3"></textarea>
      </div>
    </fieldset>

    <div class="form-group hp" aria-hidden="true">
      <label for="website">Website</label>
      <input type="text" id="website" name="website" tabindex="-1" autocomplete="off">
    </div>

    <div class="form-group form-group--submit">
      <button type="submit" class="btn btn--quote btn--large">Send quote request</button>
      <p class="form-disclaimer">Free estimate, no obligation. We reply within 72 hours.</p>
    </div>
  </form>
</section>
""")


def schema():
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "Electrician",
        "name": "Bendele Electric Inc.",
        "url": SITE,
        "image": f"{SITE}/assets/photos/truck-1600.jpg",
        "logo": f"{SITE}/assets/bendele-electric-logo.png",
        "telephone": PHONE,
        "faxNumber": "(805) 764-8636",
        "email": EMAIL,
        "description": "Family-owned electrical contractor in Santa Maria, CA, in business for 20 years. Industrial, commercial and residential electrical work. California C-10 License #881830.",
        "address": {"@type": "PostalAddress", "postOfficeBoxNumber": "1845",
                    "addressLocality": "Santa Maria", "addressRegion": "CA",
                    "postalCode": "93456", "addressCountry": "US"},
        "areaServed": [{"@type": "Place", "name": f"{t}, CA"} for t in TOWNS],
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification",
                                      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                      "opens": "07:00", "closes": "15:30"},
        "hasCredential": {"@type": "EducationalOccupationalCredential",
                          "credentialCategory": "license",
                          "name": f"California C-10 Electrical Contractor License #{LICENSE}",
                          "recognizedBy": {"@type": "Organization", "name": "Contractors State License Board"}},
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Electrical services",
                            "itemListElement": [{"@type": "Offer", "itemOffered": {
                                "@type": "Service", "name": f"{s[2]} electrical services",
                                "areaServed": "Santa Maria, CA"}} for s in SERVICES]},
    }, indent=2)


def build():
    common = dict(site=SITE, phone=PHONE, tel=TEL, email=EMAIL, license=LICENSE,
                  towns_line=", ".join(TOWNS[:-1]) + " and the " + TOWNS[-1])
    services = "\n".join(
        f'''    <article class="service" id="{key}" data-n="{n}">
      <h3 class="service__title">{title}</h3>
      <p class="service__text">{text}</p>
      <ul class="service__list">{"".join(f"<li>{i}</li>" for i in items)}</ul>
      <a class="service__link" href="quote.html?type={key}">Get {"an" if key == "industrial" else "a"} {key} quote</a>
    </article>''' for n, key, title, text, items in SERVICES)
    work = "\n".join(
        f'''    <figure class="work__item work__item--{"tall" if PHOTOS[n][1] > PHOTOS[n][0] else "wide"}">
      {pic(n, alt, "(min-width: 900px) 33vw, (min-width: 600px) 50vw, 100vw")}
      <figcaption>{cap}</figcaption>
    </figure>''' for n, cap, alt in WORK)
    towns = "\n".join(f"    <li>{t}</li>" for t in TOWNS)

    for d in DESIGNS:
        out = HERE / d["slug"]
        out.mkdir(exist_ok=True)
        styles = "\n".join(f'<link rel="stylesheet" href="{c}">' for c in d.get("css", ["style.css"]))
        common.update(styles=styles, theme=d.get("theme", "#438548"))
        home_title = "Electrician in Santa Maria, CA | Bendele Electric Inc. | Lic. #881830"
        home_desc = ("Family-owned electrical contractor in Santa Maria, CA, 20 years in business. "
                     "Industrial, commercial and residential electricians. "
                     "C-10 Lic. #881830. Call (805) 287-9044.")
        home = (HEAD.substitute(common, title=home_title, desc=home_desc, page="", kind="home",
                                fonts=d["fonts"], home="",
                                extra_head=f'<script type="application/ld+json">\n{schema()}\n</script>')
                + HOME.substitute(common, kicker=d["kicker"], h1=d["h1"], services=services, work=work,
                                  towns=towns,
                                  hero_img=pic("truck", "Bendele Electric service truck towing a scissor lift past a Santa Maria Valley vineyard",
                                               "(min-width: 900px) 55vw, 100vw", eager=True),
                                  fleet_img=pic("fleet", "Two Bendele Electric service trucks parked at a job site",
                                                "(min-width: 900px) 45vw, 100vw"))
                + FOOT.substitute(common))
        (out / "index.html").write_text(home)

        q_title = "Free Electrical Quote in Santa Maria, CA | Bendele Electric Inc."
        q_desc = ("Request a free estimate from Bendele Electric, a family-owned electrical contractor in "
                  "Santa Maria, CA. Industrial, commercial and residential. Call (805) 287-9044.")
        quote = (HEAD.substitute(common, title=q_title, desc=q_desc, page="quote.html", kind="quote",
                                 fonts=d["fonts"], home="index.html",
                                 extra_head='<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>\n'
                                            '<script src="../../quote.js" defer></script>')
                 + QUOTE.substitute(common) + FOOT.substitute(common))
        (out / "quote.html").write_text(quote)
        print("built", d["slug"])


if __name__ == "__main__":
    build()
