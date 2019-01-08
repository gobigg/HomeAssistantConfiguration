class LightSlider extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this._state = {};
  }
  set hass(hass) {
    this._hass = hass;
    const entity = hass.states[this._config.entity];
    if (entity && entity.state != this._state.state || entity.attributes.brightness != this._state.brightness) {
      this._state.state = entity.state;
      this._state.brightness = entity.attributes.brightness;
      this._updateContent(entity);
    }
  }

  setConfig(config) {
    // Check config
    if (!config.entity || config.entity.split(".")[0] !== 'light') {
      throw new Error('Please define an entity');
    }

    // Cleanup DOM
    const root = this.shadowRoot;
    if (root.lastChild) root.removeChild(root.lastChild);

    config = Object.assign({}, config);

    const card = document.createElement('ha-element');
    const style = document.createElement('style');
    style.textContent = `
            <style>
                paper-slider {width: 100%;}
            </style>
           
        `;
    card.appendChild(style);
    const content = document.createElement('div');
    content.id = "content";
    content.innerHTML = `
      <div class='state' >
        <paper-slider
          min=0
          max=255
          value=''
          step=1
          pin
          ignore-bar-touch
        ></paper-slider>
      </div>
    `;
    const slider = content.querySelector('paper-slider');
    slider.addEventListener('mouseup', ev => {
      // clear any running timeout
      clearTimeout(this._timeout);

      // start a timer to only trigger service after a period of inactivity
      this._timeout = setTimeout(() => {
        const bri = parseInt(slider.value, 10);
        if (isNaN(bri)) return;
        if (bri === 0) {
          this._hass.callService('light', 'turn_off', {
            entity_id: config.entity,
          });
        } else {
          this._hass.callService('light', 'turn_on', {
            entity_id: config.entity,
            brightness: bri,
          });
        }
      }, 1000)
    });
    card.appendChild(content);
    root.appendChild(card);
    this._config = config;
    this._content = content;
  }


  _updateContent(light) {
    const state = light.attributes.brightness
    const slider = this._content.querySelector('paper-slider');
    // update only value
    slider.value = state;
  }
}

customElements.define('light-slider', LightSlider);