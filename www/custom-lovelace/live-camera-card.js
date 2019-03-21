
import {
    LitElement, html
  } from 'https://unpkg.com/@polymer/lit-element@^0.5.2/lit-element.js?module';
  
  class LiveCameraCard extends LitElement {
    /* eslint-disable indent,object-curly-newline */
    _render({ camera, updateInterval }) {
      const accessToken = camera && this._hass.states[camera].attributes.access_token;
      const template = html`
      <style>
        .container {
          display: flex;
          align-items: stretch;
          background: #000;
        }

        .image {
          flex: 3;
          height: 100%;
          position: relative;
          display: flex;
          align-items: center;
          justify-content: center;
          overflow: hidden;
        }
  
        .image > img {
          display: inline-block;
          max-width: 100%;
          max-height: 100%;
        }

      </style>
      <ha-card on-tap="${ev => this._toggle(this.camera)}">
        <div class="container">
          <div class="image">
            <img src$="${this.camera ? `/api/camera_proxy_stream/${this.camera}?token=${accessToken}&interval=${updateInterval}` : ''}" />
          </div>
        </div>
      </ha-card>
      `;
  
      return template;
    }
    /* eslint-enable indent,object-curly-newline */
  
    static get properties() {
      return {
        _hass: Object,
        camera: String,
        updateInterval: Number
      };
    }
  
    setConfig(config) {
      this.camera = config.camera;
      this.updateInterval = config.update_interval || 1;
    }
    
    _toggle(camera) {

        const node = this.shadowRoot;
        const options = {};
        const detail = { entityId: camera };
        const event = new Event('hass-more-info', {
          bubbles: options.bubbles === undefined ? true : options.bubbles,
          cancelable: Boolean(options.cancelable),
          composed: options.composed === undefined ? true : options.composed,
        });
        event.detail = detail;
        node.dispatchEvent(event);
        return event;
  }
    
  
    set hass(hass) {
      this._hass = hass;
    }
    
  }
  customElements.define('live-camera-card', LiveCameraCard);