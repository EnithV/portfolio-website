(function () {
  const navbar = document.querySelector(".site-navbar");
  const navLinks = document.querySelectorAll(".site-navbar .nav-link[data-section]");
  const sections = [...navLinks].map((l) => document.getElementById(l.dataset.section)).filter(Boolean);

  /* Navbar shadow on scroll */
  const onScroll = () => {
    if (navbar) navbar.classList.toggle("scrolled", window.scrollY > 24);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Active nav link */
  if (sections.length && navLinks.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            navLinks.forEach((link) => {
              link.classList.toggle("active", link.dataset.section === id);
              if (link.dataset.section === id) {
                link.setAttribute("aria-current", "page");
              } else {
                link.removeAttribute("aria-current");
              }
            });
          }
        });
      },
      { rootMargin: "-30% 0px -60% 0px", threshold: 0 }
    );
    sections.forEach((s) => observer.observe(s));
  }

  /* Project filter */
  const filterInputs = document.querySelectorAll('input[name="projectFilter"]');
  const projectItems = document.querySelectorAll(".project-item");

  filterInputs.forEach((input) => {
    input.addEventListener("change", () => {
      const value = input.value;
      projectItems.forEach((item) => {
        const tags = (item.dataset.tags || "").split(",");
        const show = value === "all" || tags.includes(value);
        item.classList.toggle("hidden", !show);
      });
    });
  });

  /* Close mobile menu on nav click */
  const navCollapse = document.getElementById("navbarNav");
  const closeMobileNav = () => {
    if (navCollapse?.classList.contains("show")) {
      bootstrap.Collapse.getOrCreateInstance(navCollapse).hide();
    }
  };
  navLinks.forEach((link) => link.addEventListener("click", closeMobileNav));
  document.querySelector(".brand-lockup")?.addEventListener("click", closeMobileNav);
})();
