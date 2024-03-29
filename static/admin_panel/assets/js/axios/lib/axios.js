'use strict';

import utils from 'axios/lib/utils.js';
import bind from 'axios/lib/helpers/bind.js';
import Axios from 'axios/lib/core/Axios.js';
import mergeConfig from 'axios/lib/core/mergeConfig.js';
import defaults from 'axios/lib/defaults/index.js';
import formDataToJSON from 'axios/lib/helpers/formDataToJSON.js';
import CanceledError from 'axios/lib/cancel/CanceledError.js';
import CancelToken from 'axios/lib/cancel/CancelToken.js';
import isCancel from 'axios/lib/cancel/isCancel.js';
import {VERSION} from 'axios/lib/env/data.js';
import toFormData from 'axios/lib/helpers/toFormData.js';
import AxiosError from 'axios/lib/core/AxiosError.js';
import spread from 'axios/lib/helpers/spread.js';
import isAxiosError from 'axios/lib/helpers/isAxiosError.js';
import AxiosHeaders from "axios/lib/core/AxiosHeaders.js";
import HttpStatusCode from 'axios/lib/helpers/HttpStatusCode.js';

/**
 * Create an instance of Axios
 *
 * @param {Object} defaultConfig The default config for the instance
 *
 * @returns {Axios} A new instance of Axios
 */
function createInstance(defaultConfig) {
  const context = new Axios(defaultConfig);
  const instance = bind(Axios.prototype.request, context);

  // Copy axios.prototype to instance
  utils.extend(instance, Axios.prototype, context, {allOwnKeys: true});

  // Copy context to instance
  utils.extend(instance, context, null, {allOwnKeys: true});

  // Factory for creating new instances
  instance.create = function create(instanceConfig) {
    return createInstance(mergeConfig(defaultConfig, instanceConfig));
  };

  return instance;
}

// Create the default instance to be exported
const axios = createInstance(defaults);

// Expose Axios class to allow class inheritance
axios.Axios = Axios;

// Expose Cancel & CancelToken
axios.CanceledError = CanceledError;
axios.CancelToken = CancelToken;
axios.isCancel = isCancel;
axios.VERSION = VERSION;
axios.toFormData = toFormData;

// Expose AxiosError class
axios.AxiosError = AxiosError;

// alias for CanceledError for backward compatibility
axios.Cancel = axios.CanceledError;

// Expose all/spread
axios.all = function all(promises) {
  return Promise.all(promises);
};

axios.spread = spread;

// Expose isAxiosError
axios.isAxiosError = isAxiosError;

// Expose mergeConfig
axios.mergeConfig = mergeConfig;

axios.AxiosHeaders = AxiosHeaders;

axios.formToJSON = thing => formDataToJSON(utils.isHTMLForm(thing) ? new FormData(thing) : thing);

axios.HttpStatusCode = HttpStatusCode;

axios.default = axios;

// this module should only have a default export
export default axios
