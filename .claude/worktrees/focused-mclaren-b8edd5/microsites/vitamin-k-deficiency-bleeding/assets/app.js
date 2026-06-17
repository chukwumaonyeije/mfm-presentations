(function () {
  // Footer year
  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  // View toggle functionality
  const toggleBtn = document.getElementById("toggleView");
  const toggleLabel = toggleBtn.querySelector(".toggle-label");

  // Check for saved preference
  const savedView = localStorage.getItem("vk-view");
  if (savedView === "clinician") {
    document.body.classList.add("show-clinician");
    toggleLabel.textContent = "Patient view";
  }

  toggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("show-clinician");
    const isClinicianView = document.body.classList.contains("show-clinician");
    toggleLabel.textContent = isClinicianView ? "Patient view" : "Clinician view";
    localStorage.setItem("vk-view", isClinicianView ? "clinician" : "patient");
  });

  // Accessible accordion behavior
  const accordions = document.querySelectorAll("[data-accordion]");
  accordions.forEach((root) => {
    const buttons = root.querySelectorAll(".accordion-item");
    buttons.forEach((btn) => {
      const panel = btn.nextElementSibling;
      if (!panel) return;

      btn.addEventListener("click", () => toggle(btn, panel));
      btn.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          toggle(btn, panel);
        }
      });
    });

    function toggle(btn, panel) {
      const expanded = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!expanded));
      panel.hidden = expanded;

      const icon = btn.querySelector(".accordion-icon");
      if (icon) icon.textContent = expanded ? "+" : "–";
    }
  });
})();
