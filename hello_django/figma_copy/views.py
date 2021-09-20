from django.http import HttpResponse
def figma_copy(request):
    html="""<html><link type="text/css" rel="stylesheet" id="dark-mode-custom-link"><link type="text/css" rel="stylesheet" id="dark-mode-general-link"><style lang="en" type="text/css" id="dark-mode-custom-style"></style><style lang="en" type="text/css" id="dark-mode-native-style"></style><head>
    <meta charset="utf-8">

    <script nonce="">
      if (function() {
        try { eval('(async () => { for await (let v of [{ async* [Symbol.asyncIterator]() { yield {x: 1} } }]) { let {a, ...b} = {...v} } })().finally(() => {}); /\\p{Z}/u;') } catch (e) { return true }

        return false
      }()) {
        location.href = '/unsupported_browser'
      }
    </script>



    <script nonce="">
  (function() {
    if (!window.INITIAL_OPTIONS) {
      window.INITIAL_OPTIONS = {};
    }

    window.INITIAL_OPTIONS.feature_flags = {"agent_new_installs":true,"antispam_rl_invite_from_new_user":true,"antispam_rl_org":true,"aus_locked_orgs":true,"aus_minimal_orgs":true,"batch_component_actions":true,"block_auth_for_disposable_emails":true,"branching_and_merging_creation":true,"branching_and_merging_onFrame":true,"branching_and_merging_reviews":true,"branching_and_merging_reviews_lg":true,"browse_ia":true,"browse_ia_settings_modal":true,"check_higher_buffer_version":true,"check_replica_lag":true,"cjk_extended_font_fallback":true,"clear_received_join_end":true,"community_comments_mentions":true,"community_hub_ga":true,"community_hub_image_inspection":true,"community_org_team_ia":true,"community_pop_score_replica":true,"community_show_related_content":true,"copy_properties_from_menu":true,"csp_prod":true,"csp_prod_admin":true,"csp_prod_admin_enforce":true,"csp_prod_enforce":true,"cursor_chat":true,"db_request_reconnect":true,"deep_search_indexing":true,"deep_search_live_launch":true,"defer_invisible_children":true,"defer_update_default_style":true,"disable_long_frame_time":true,"ds_move_component":true,"ds_replace_libraries":true,"edu_onboarding_grace_period":true,"edu_onboarding_verification_form":true,"edu_verification_form_updated":true,"ee_bring_forward_visibly":true,"ee_knockout_shadow":true,"ee_svg_shape_rendering":true,"enable_exp_branching_filter":true,"exp_branching":true,"exp_edu_onboarding_acc_creation":true,"exp_figjam_editor_nudge_v1":true,"exp_guest_management_admin":true,"exp_request_to_edit_orgs":true,"exp_request_to_edit_teams":true,"exp_workshop_mode_orgs":true,"exp_workshop_mode_teams":true,"explicitly_schedule_frames":true,"figjam_allow_paste_into_design":true,"figjam_bug_button_support":true,"figjam_copy_paste_offset":true,"figjam_export":true,"figjam_ga":true,"figjam_high_fives":true,"figjam_high_fives_use_os_cursor":true,"figjam_import_parse_html":true,"figjam_launch_announcement":true,"figjam_launch_browser":true,"figjam_launch_growth":true,"figjam_ngima_stickers":true,"figjam_off":true,"figjam_plugins":true,"figjam_plugins_relaunch_buttons":true,"figjam_plugins_rich_if_apis":true,"figjam_plugins_templates":true,"figjam_plugins_validation":true,"figjam_show_bug_button":true,"figjam_templates_new_file_topbar":true,"figma_design_cursor_chat":true,"font_enable_vf_instances":true,"font_skip_inter":true,"font_skip_sf_pro":true,"free_tier_refresh_launch":true,"frontend_sentry_errors":true,"fullscreen_alt_drag_delay":true,"fullscreen_pen_tool_memory":true,"gc_component_actions":true,"generate_checkpoint_thumbnails":true,"get_file_pixie_worker":true,"gtm_geolocation":true,"hand_cursor_press_state":true,"hardware_acceleration_warning":true,"i18n_split_defer_to_client_auth":true,"image_crop_shortcut":true,"improved_team_member_loading":true,"livegraph_better_optimistic":true,"livegraph_idle_disconnect":true,"livegraph_user_state":true,"menu_search_metrics_tracker":true,"migrate_checkpoint_version":true,"migrate_community_files":true,"migrate_styles":true,"missing_fonts_dialog":true,"modal_dropdown_menus":true,"multiplayer_checkpoints_180":true,"multiplayer_checkpoints_75":true,"multiplayer_figjam_max_conn_500":true,"multiplayer_hide_cursors":true,"multiplayer_migrate_pending":true,"multiplayer_migration_fpm":true,"multiplayer_reconnect_seq_num":true,"multiplayer_scene_val_sentry":true,"multiplayer_scene_validation":true,"multiplayer_style_canvas_val":true,"multiplayer_suppress_broadcast":true,"multiplayer_zstd_compression":true,"org_downgrade_multi_transaction":true,"org_merges_multi_transaction":true,"org_migration_locking":true,"org_migration_multi_transaction":true,"org_migration_multi_tx_ss":true,"org_ops_locked":true,"org_user_import_multi_tx":true,"overwrite_file_thumbnails":true,"parameterized_plugins":true,"pencil_shift_to_straight":true,"pixie_use_file_proxy_fallback":true,"pre_figjam_launch_promo":true,"prevent_instance_style_dirty":true,"pro_figjam_file_edit_link":true,"pro_team_dashboard":true,"pro_team_user_checkpoint_upgrade":true,"prototype_lib_fetch_shared_fonts":true,"prototype_lib_missing_fonts_alt":true,"prototype_multiple_entry_points":true,"prototype_view_refactor":true,"quick_commands_floating_search":true,"quick_commands_metrics_tracker":true,"quick_commands_popularity_rank":true,"random_page_rampup":true,"recaptcha_frontend_web":true,"recaptcha_serverside_enforce":true,"remote_work_templates":true,"report_lower_buffer_version":true,"request_to_edit":true,"require_okta_groups_reject":true,"security_logging_firehose":true,"selection_paints_deleted_style":true,"show_menu_item_al_symbol_repub":true,"show_state_group_size_errors":true,"solid_second_paint":true,"sso_autodirect":true,"starter_file_edit_link":true,"streamline_figjam_onboarding":true,"survey_org_cart_abandon":true,"survey_pro_cart_abandon":true,"tax_excluded":true,"team_org_moves_multi_transaction":true,"text_wrapping_improvements":true,"use_absolute_bounds_export":true,"use_appconfig":true,"user_pref_sync":true,"ux_feedback_survey":true,"viewer_dedup_prototype_state":true,"viewer_drop_shadow_move_ssg":true,"viewer_fix_ctg_memory_bloat":true,"viewer_no_dup_data_on_prm":true,"viewer_observation_v2":true,"viewer_simple_slides_condition":true,"viewer_ssaa_only_lower_dpr":true,"vitess_async_reads":true,"vitess_async_writes":true,"vitess_connect_without_dbname":true,"vitess_egc_force_sync":true,"vitess_fig_images_read_perc":true,"vitess_fig_images_write_perc":true,"vitess_wait_for_results":true,"voice_audio_in_cursor":true,"voice_enabled":true,"voice_rollout":true,"voice_unmute_on_join":true};
      window.INITIAL_OPTIONS.interactive_components_beta = false;
    window.INITIAL_OPTIONS.tracking_session_id = "KWHvbjZuYvhQd5en";
    window.INITIAL_OPTIONS.cluster_name = "prod";
    window.INITIAL_OPTIONS.error_dashboard_url = "https://errors.figma.com/api";
    window.INITIAL_OPTIONS.frontend_sentry_dsn = "https://d1b12a8fbe424e4b956eb33cadd5b30d@errors.figma.com/api/sentry/56203";
    window.INITIAL_OPTIONS.figma_email_suffix = "@figma.com";
    window.INITIAL_OPTIONS.csp_nonce = "WgHrpWmPfnIg/WI/CppKrQ==";
    window.INITIAL_OPTIONS.figma_url = "https://www.figma.com";

    window.INITIAL_OPTIONS.flash = {
      error: null,
      warn: null,
      success: null
    }

      window.INITIAL_OPTIONS.user_flags = [{"id":338636841,"user_id":1019473611201361470,"name":"not_gen_0","created_at":"2021-09-14T05:04:09.922Z","updated_at":"2021-09-14T05:04:09.922Z"},{"id":338636842,"user_id":1019473611201361470,"name":"opted_in_email","created_at":"2021-09-14T05:04:09.936Z","updated_at":"2021-09-14T05:04:09.936Z"},{"id":338636840,"user_id":1019473611201361470,"name":"use_numbers_for_opacity","created_at":"2021-09-14T05:04:09.908Z","updated_at":"2021-09-14T05:04:09.908Z"}]
      window.INITIAL_OPTIONS.user_data = {"id":"1019473611201361470","name":"KUSHAGRA PATIDAR","email":"kushagra24ai027@satiengg.in","handle":"KUSHAGRA PATIDAR","img_url":"https://www.gravatar.com/avatar/906008551811db602a746ab128f338fa?size=240\u0026default=https%3A%2F%2Fs3-alpha.figma.com%2Fstatic%2Fuser_k_v2.png","created_at":"2021-09-14T05:04:09.806Z","email_validated_at":"2021-09-14T05:04:09.988Z","unsubscribed_at":null,"utc_offset":null,"profile":{"job_title":"software-development","usage_purpose":"For work"},"phone_number":null,"student_validated_at":null,"description":null,"plugin_publishing_blocked_at":null,"community_commenting_blocked_at":null,"dev_tokens":[],"oauth_tokens":[],"realtime_token":"/me-1019473611201361470:1631595863:0:6a64b9596baf8c6815bf346e05691753555200aa","realtime_token_inactive":"/user-inactive-1019473611201361470:1631595863:0:bf394b1ba30dac2ff64e15947358899642838198","two_factor_enabled":false,"two_factor_app_enabled":false,"google_sso_only":"2021-09-14T05:04:09.802Z","saml_sso_only":false,"experiment_seed":"114967","community_profile_id":null,"community_profile_handle":null,"community_beta_at":null,"locale":"en","experiment_assignments":[],"teams":[{"id":"1019468225053205209","name":"Web Squad","created_at":"2021-09-14T04:42:45.649Z","img_url":null,"synced_at":null,"providers":null,"stripe_customer_id":null,"subscription":null,"editors":1,"projects":1,"student_team_at":null,"student_autoverifying_team_at":null,"grace_period_end":null,"org_id":null,"img_urls":null,"org_access":null,"deleted_at":null,"blocked_at":null,"trial_period_end":null,"description":null,"deleted_by":null,"experiment_seed":546471,"workspace_id":null,"restrictions_list":["projects_limited"],"student_team":false,"community_profile_id":null,"community_profile_handle":null,"is_paid":false,"experiment_assignments":[]}]};
      window.INITIAL_OPTIONS.smart_token = "stv2-1019473611201361470-a8a12cc48276db01ffc5717bdca8ec8c4b3897abc849d876e85f862b3214a551-1631595849";
      window.wootricSettings = {
        email: window.INITIAL_OPTIONS.user_data.email,
        created_at: Math.floor(new Date(window.INITIAL_OPTIONS.user_data.created_at).getTime() / 1000),
        account_token: "NPS-8d7627ca",
        product_name: 'Figma',
      };

      var _initial_options = {"resource_type":null,"email":"kushagra24ai027@satiengg.in","user_ip":"49.15.183.32","redirect_url":null,"email_token":null,"access_code":null,"existing_session":true,"editing_file":null,"zeplin_plugin_id":"745330164019088593","avocode_plugin_id":"821674268995163810","org_id":null,"is_cloudfront":true,"iso_code":"IN","viewer_city":"Indore"}
      for (var key in _initial_options) {
        window.INITIAL_OPTIONS[key] = _initial_options[key]
      }

    window.EARLY_ARGS = window.EARLY_ARGS || {};
    window.EARLY_ARGS.omit_core_data = false;
    window.EARLY_ARGS.file_minimal_user_state = false;

      window.INITIAL_OPTIONS.user_notifications_bell = { bell: {"0":false} }
      window.INITIAL_OPTIONS.promo = null

      window.Fig = window.Fig || {};
      var _figOptions = {"importShimURL":"https://static.figma.com/fullscreen/d26937d75bdf683235c614a9a57cac3ca4c2a46a/import.shim.js.br","importWorkerURL":"https://static.figma.com/fullscreen/d26937d75bdf683235c614a9a57cac3ca4c2a46a/import.worker.js.br","figMigratorURL":"https://static.figma.com/fullscreen/d79c7ae91e91d26d4e33d8e322a2e41172bb7805/fig_migrator.js.br","jsvmCppURLs":{"jsvm-cpp.js":"https://static.figma.com/fullscreen/da00c86749491ba844de40ae0a1dcaae6da17aaf/jsvm-cpp.js.br","jsvm-cpp.wasm":"https://static.figma.com/fullscreen/da00c86749491ba844de40ae0a1dcaae6da17aaf/jsvm-cpp.wasm.br"},"fullscreenURLs":{"compiled_wasm.js":"https://static.figma.com/fullscreen/6ec1792e764602e75d392be212aaf69990b23434/compiled_wasm.js.br","compiled_wasm.wasm":"https://static.figma.com/fullscreen/6ec1792e764602e75d392be212aaf69990b23434/compiled_wasm.wasm.br"},"fullscreenScriptHash":"7ecb0a0b8467dab2218988818f261c9db141719f","librarySearchWorkerURL":"https://www.figma.com/figbuild-artifacts/library_search_worker.6055c05bff4e3bf0f98764a983550ea1.min.js.br","migrationURLs":{"file_migrations_wasm.js":"https://static.figma.com/fullscreen/6ec1792e764602e75d392be212aaf69990b23434/file_migrations_wasm.js","file_migrations_wasm_bg.wasm":"https://static.figma.com/fullscreen/6ec1792e764602e75d392be212aaf69990b23434/file_migrations_wasm_bg.wasm"},"viewerScriptURL":"https://static.figma.com/fullscreen/6ec1792e764602e75d392be212aaf69990b23434/viewer.js.br","viewerWorkerURL":"https://static.figma.com/fullscreen/6ec1792e764602e75d392be212aaf69990b23434/imagedecoder.js.br"};
      for (var key in _figOptions) {
        Fig[key] = _figOptions[key]
      }

      const pro_trial_json = {"pro_trials_v2_published_team_library":{"default":{"file_name":"Music App Design Library","file_key":"D3JUit9Sj3zA01jZ2yIeAW","checkpoint_id":905230943858114618,"folder_name":"Pro Trial Checklist"}},"pro_trials_v2_imported_component":{"published_components":{"file_name":"Music App","file_key":"EPsAVfTmWm0rTWWt1xTThr","checkpoint_id":905231385563295691,"folder_name":"Pro Trial Checklist"},"local_components":{"file_name":"Music App","file_key":"aJNeFFEcSww5Fkj8YB882S","checkpoint_id":905231650961895864,"folder_name":"Pro Trial Checklist"},"component_name":"Play Button"}}

      if (!!pro_trial_json.pro_trials_v2_imported_component) {
        const imported_component_json = pro_trial_json.pro_trials_v2_imported_component
        if (!!imported_component_json.published_components) {
          window.INITIAL_OPTIONS.pro_trials_v2_imported_component_file_name = pro_trial_json.pro_trials_v2_imported_component.published_components.file_name
        }
        window.INITIAL_OPTIONS.pro_trials_v2_component_name = imported_component_json.component_name
      }

      if (!!pro_trial_json.pro_trials_v2_published_team_library) {
        const published_team_library_json = pro_trial_json.pro_trials_v2_published_team_library
        if (!!published_team_library_json.default) {
          window.INITIAL_OPTIONS.pro_trials_v2_published_team_library_file_name = published_team_library_json.default.file_name
        }
      }


      window.INITIAL_OPTIONS.segment_web_key = "6Zhdn0wK1GLYzCsb0LIK0oQplS5TXcB2"

      window.INITIAL_OPTIONS.segment_fullscreen_key = "6uxDivlUmLf95lHRk0R8bZvr8zDxbX5E"

      window.INITIAL_OPTIONS.zendesk_web_key_public = "8f3196e1-a5a9-4a39-9b1c-6ab81db7fe17"

      window.INITIAL_OPTIONS.stripe_api_public = "pk_live_LKZ0RKjSZG2D2pwdtwrAhkiJ"

      window.INITIAL_OPTIONS.google_tag_manager_iframe_url = "https://marketing.figma.com"

    window.INITIAL_OPTIONS.recaptcha_v3_ent_site_key = "6Le0W80aAAAAAGU9L7qz4o9tQVqrdJVv2M8XHIcd"

    window.INITIAL_OPTIONS.release_manifest_hash = "b5afaafc84db6d334777c72c48584768"

      console.log('Running frontend commit', "4280a2a1d706f5fa73fe6a6f1cbca4dcdf526db2")

      window.INITIAL_OPTIONS.release_manifest_git_commit = "4280a2a1d706f5fa73fe6a6f1cbca4dcdf526db2"
      window.INITIAL_OPTIONS.release_server_git_commit = "fcfdb843494fea1c1178711eef31051770853807"
      window.INITIAL_OPTIONS.release_git_tag = "release-2021-09-13"
  })();
</script>
<script nonce="">
window.FIGMA_BUNDLE = (function () {
  const pathsForModules = (() => {
    const _paths = {

    };

    const _loadedPaths = new Set()
    return {
      get: (key) => {
        return _paths[key];
      },
      hasLoaded: (key) => {
        return _loadedPaths.has(key)
      },
      setHasLoaded: (key) => {
        return _loadedPaths.add(key)
      },
    };
  })();

  const values = {};
  const promises = {};

  return {
    export: function (name, value) {
      if (!pathsForModules.get(name)) {
        console.warn('please add the "js_path" declaration in "pathsForModules" for "' + name + '".');
        return;
      }
      values[name] = value;
    },

    import: function (name) {
      const FAILURE_TEXT = 'failed to load "' + name + '" module!'
      if (values[name]) return Promise.resolve(values[name])

      const path = pathsForModules.get(name);
      if (!pathsForModules.get(name)) {
        return Promise.reject({ error: FAILURE_TEXT + ' "' + name + '" has not been added to "pathsForModules".' })
      }

      if (promises[path]) {
        return new Promise((resolve, reject) => {
          promises[path].then(_ => resolve(values[name])).catch(error => reject({ error }));
        });
      }

      const promise = new Promise((resolve, reject) => {
        if (promises[path]) return;

        const script = document.createElement("script");
        script.setAttribute("async", true);
        script.setAttribute("nonce", "WgHrpWmPfnIg/WI/CppKrQ==")

        script.onload = function () {
          resolve(values[name])
        };
        script.onerror = function (error) {
          reject(error)
        };

        script.src = pathsForModules.get(name);
        pathsForModules.setHasLoaded(name);
        document.body.appendChild(script)
      });
      promises[path] = promise;
      return promise;
    },
  };
})();
</script>
  <script nonce="">
    (function(t){var e={},r=function(){return this}();return function n(o){var s=e[o];return s?s.exports:(s=e[o]={exports:{},id:o,loaded:!1},t[o].call(r,s,s.exports,n),s.exports instanceof Function&&(s.exports.default=s.exports),s.loaded=!0,s.exports)}(t.length-1)})([
(function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),self.global=self;const o=e=>{var t;const s=null===(t=window.INITIAL_OPTIONS.user_data)||void 0===t?void 0:t.id,o=window.INITIAL_OPTIONS.tracking_session_id,i=window.INITIAL_OPTIONS.release_manifest_git_commit;window.mpGlobal={version:56,sock:null,msgs:[],perfMetrics:[],url({fileKey:t,role:n,oauthToken:r,nodeIds:a}){let w=null;e&&t===e.fileKey&&e.targetFileVersion&&(w=e.targetFileVersion);let d="";"editor"!==n&&"viewerWithCpp"!==n||!a||(d=`&scenegraph-queries-initial-nodes=${a}`);const l=window.INITIAL_OPTIONS.feature_flags,p="editor"===n&&l.multiplayer_zstd_compression||"viewerWithCpp"===n&&l.multiplayer_zstd_compression||("prototype"===n||"viewer"===n)&&l.viewer_multiplayer_zstd;return`${location.protocol.replace("http","ws")}//${location.host}/api/multiplayer/${t}?role=${n}`+`&tracking_session_id=${o}&version=${this.version}`+(r?"&oauth_token="+r:"")+d+(p?"&compression=zstd":"")+(s?`&user-id=${s}`:"")+(w?`&target-file-version=${w}`:"")+(i?`&client_release=${i}`:"")},preconnect(e){if(this.sock){if(e===this.sock.url&&this.sock.readyState!==WebSocket.CLOSED)return;try{this.sock.close()}catch(t){}}this.sock=new WebSocket(e),this.sock.binaryType="arraybuffer",this.sock.onopen=(e=>{this.perfMetrics.push({key:"mp-ws-onopen",ts:performance.now(),nBytes:void 0})}),this.sock.onmessage=(e=>{const t=new Uint8Array(e.data);this.msgs.push(t),this.perfMetrics.push({key:"mp-ws-onmessage",ts:performance.now(),nBytes:t.length*t.BYTES_PER_ELEMENT})}),this.msgs=[],this.perfMetrics=[]}},e&&mpGlobal.preconnect(mpGlobal.url(e))};(()=>{const{file_minimal_user_state:e,mock_user_state_for_tests_json:t,multiplayer_preconnect_options:s,omit_core_data:i}=window.EARLY_ARGS||{};window.INITIAL_OPTIONS||(window.INITIAL_OPTIONS={}),((e,t,s)=>{if(e)window.userStateXHR={readyState:4,status:200,responseText:e};else if(window.Fig){if(!window.INITIAL_OPTIONS.user_data)return void(window.startUserStateXHR=(()=>{}));window.startUserStateXHR=function(e){var t,o="/api/user/state",i=[];window.INITIAL_OPTIONS.org_id&&i.push("org_id="+window.INITIAL_OPTIONS.org_id),i.push("omit_user_flags=1"),i.push("omit_file_browser_preferences=1"),s&&i.push("omit_core_data=1"),e&&i.push("file_key="+e),0!==i.length&&(o+="?"+i.join("&")),window.userStateXHR=new XMLHttpRequest,window.userStateXHR.open("GET",o);const n=null===(t=window.INITIAL_OPTIONS.user_data)||void 0===t?void 0:t.id;n&&window.userStateXHR.setRequestHeader("X-Figma-User-ID",n),window.userStateXHR.send();var r=window.performance?window.performance.now():-1;window.userStateXHR.addEventListener("load",function(){window.userStateXHRDuration=window.performance?window.performance.now()-r:-1},!1),window.sessionStateXHR=new XMLHttpRequest,window.sessionStateXHR.open("GET","/api/session/state"),n&&window.sessionStateXHR.setRequestHeader("X-Figma-User-ID",n),window.sessionStateXHR.send()};const e="/preload-editor"===location.pathname||"/file/new"===location.pathname,o=window.INITIAL_OPTIONS.editing_file&&window.INITIAL_OPTIONS.editing_file.key;t?window.startUserStateXHR(o):e||window.startUserStateXHR()}})(t,e,i),o(s)})()})]);

//# sourceMappingURL=https://admin.figma.com/admin/figbuild-artifacts/early.834c2ff85480fa9d9838e6b7a110ac4e.min.js.map
  </script>


    <meta name="google" content="notranslate">
    <meta name="slack-app-id" content="A01N2QYSA81">

    <title>Web Squad – Figma</title>

    <style type="text/css">
  #filebrowser-loading-page {
    opacity: 1;
    -webkit-transition: opacity .2s ease-in-out;
    display: flex;
    flex-wrap: wrap;

    /* Make sure the loading page is flush with the edges of the page so
       our layout isnt affected by browser default margins/paddings */
    position: absolute;
    top: 48px;
    bottom: 0;
    left: 0;
    right: 0;
  }

  #filebrowser-loading-page.fadeOut {
    opacity: 0;
  }

  #filebrowser-loading-page.hidden {
    display: none;
    opacity: 0;
  }

 /*
  * HAX: The sidebar is cloned and used independently outside of this
  * page so any styles like `#filebrowser-loading-page .thing` applied
  * to sidebar sub-elements also need a selector like
  * `.filebrowser-loading-sidebar .thing` so that they work outside of
  * this page too.
  */
  #filebrowser-loading-page .row,
  .filebrowser-loading-sidebar .row {
    background-color: #f0f0f0;
    border-radius: 3px;
    height: 16px;
  }

  #filebrowser-loading-page .circle,
  .filebrowser-loading-sidebar .circle {
    border-radius: 50%;
    background-color: #f0f0f0;
    width: 22px;
    height: 22px;
  }

  #filebrowser-loading-page .row .circle,
  .filebrowser-loading-sidebar .row .circle {
    position: relative;
    top: -3px;
    left: -35px;
  }

  .filebrowser-loading-sidebar {
    flex: 0 0 224px;
    background-color: white;
    padding-top: 8px;
    display: flex;
    flex-direction: column;
  }

  #filebrowser-loading-page .navbar {
    height: 48px;
    width: 100%;
    position: fixed;
    top: 0;
    background-color: #2C2C2C;
    z-index: 1;
  }

  .filebrowser-loading-sidebar .row {
    width: 85px;
    margin-top: 8px;
    margin-bottom: 8px;
    margin-left: 48px;
  }

  .filebrowser-loading-sidebar .row .circle {
    position: relative;
    top: -3px;
    left: -35px;
  }

  #filebrowser-loading-page .divider,
  .filebrowser-loading-sidebar .divider {
    height: 1px;
    background-color: rgba(0, 0, 0, 0.1);
    margin-top: 8px;
    margin-bottom: 8px;
  }

  .filebrowser-loading-sidebar .row:nth-child(2) { width: 40px; }
  .filebrowser-loading-sidebar .row:nth-child(3) { width: 58px; }
  .filebrowser-loading-sidebar .row:nth-child(4) { width: 58px; }
  .filebrowser-loading-sidebar .row:nth-child(7) { width: 60px; }
  .filebrowser-loading-sidebar .row:nth-child(8) { margin-left: 16px; margin-right: 16px; }
  .filebrowser-loading-sidebar .row:nth-child(9) { width: 60px; }
  .filebrowser-loading-sidebar .row:nth-child(10) { width: 46px; opacity: .8; }
  .filebrowser-loading-sidebar .row:nth-child(11) { width: 65px; opacity: .4; }

  #filebrowser-loading-page .page {
    flex: 1 1;
    box-sizing: border-box;
    border-left: 1px #e5e5e5 solid;
    display: flex;
    flex-direction: column;
  }

  #filebrowser-loading-page .toolbar {
    border-bottom: 1px #e5e5e5 solid;
    height: 48px;
  }

  #filebrowser-loading-page .toolbar .item {
    background-color: #f0f0f0;
    border-radius: 3px;
    width: 85px;
    height: 16px;
    margin-left: 32px;
    margin-top: 16px;
  }

  #filebrowser-loading-page .columns {
    flex: 1 1;
    display: flex;
    flex-direction: row-reverse;
    padding-right: 32px;
  }

  @media (max-width: 849px) {
    #filebrowser-loading-page .columns {
      flex-direction: column;
    }

    #filebrowser-loading-page .right-column {
      padding-left: 32px;
    }

    #filebrowser-loading-page .public-header + .columns {
      flex-direction: column-reverse;
    }
  }

  #filebrowser-loading-page .content {
    flex: 1 1;
  }

  #filebrowser-loading-page .sort-dropdown {
    background-color: #f0f0f0;
    border-radius: 3px;
    width: 72px;
    height: 16px;
    margin: 24px 32px;
  }

  #filebrowser-loading-page .tile {
    height: 0;
    padding-top: 75%;
    box-sizing: border-box;
    position: relative;
  }

  #filebrowser-loading-page .tile .inner {
    position: absolute;
    top: 2px;
    bottom: 2px;
    left: 2px;
    right: 2px;
    border: 1px solid #f0f0f0;
    border-radius: 6px;
    background-color: #f0f0f0;
  }

  #filebrowser-loading-page .tile .inner .lower {
    height: 54px;
    background-color: white;
    position: absolute;
    bottom: 0;
    width: 100%;
    border-radius: 0 0 6px 6px;
  }

  #filebrowser-loading-page .public-grid {
    width: 100%;
    box-sizing: border-box;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(256px, 1fr));
    grid-gap: 32px;
    padding-left: 32px;
  }

  @media (max-width: 1023px) {
    #filebrowser-loading-page .public-grid {
      grid-template-columns: 1fr;
    }
  }

  #filebrowser-loading-page .public-grid .tile {
    height: 0px;
    padding-top: 75%;
  }

  #filebrowser-loading-page .public-grid .tile:nth-child(6) { opacity: .8; }
  #filebrowser-loading-page .public-grid .tile:nth-child(7) { opacity: .4; }

  #filebrowser-loading-page .file-grid {
    width: 100%;
    box-sizing: border-box;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(256px, 1fr));
    grid-gap: 32px;
    padding-left: 32px;
  }

  #filebrowser-loading-page .file-grid .tile:nth-child(6) { opacity: .8; }
  #filebrowser-loading-page .file-grid .tile:nth-child(7) { opacity: .4; }

  #filebrowser-loading-page .team-grid {
    width: 100%;
    box-sizing: border-box;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(264px, 1fr));
    grid-gap: 32px 32px;
    padding: 32px 0 0 32px;
    align-content: start;
  }

  #filebrowser-loading-page .team-tile {
    border: 1px solid rgba(0, 0, 0, .1);
    border-radius: 6px;
    position: relative;
    padding: 16px;
  }

  #filebrowser-loading-page .team-grid .team-tile:nth-child(6) { opacity: .8; }
  #filebrowser-loading-page .team-grid .team-tile:nth-child(7) { opacity: .4; }

  #filebrowser-loading-page .team-tile .row {
    margin-top: 0;
    margin-left: 0;
    margin-bottom: 0;
  }

  #filebrowser-loading-page .team-tile .row:nth-child(1) {
    width: 32px;
    height: 32px;
  }

  #filebrowser-loading-page .team-tile .row:nth-child(2) {
    width: 65px;
    height: 30px;
    position: absolute;
    top: 17px;
    right: 16px;
    margin-top: 0;
  }

  #filebrowser-loading-page .team-tile .row:nth-child(3) {
    width: 120px;
    margin-top: 20px;
  }
  #filebrowser-loading-page .team-tile .row:nth-child(4) {
    width: 232px;
    margin-top: 12px;
  }
  #filebrowser-loading-page .team-tile .row:nth-child(5) {
    width: 174px;
    margin-top: 8px;
  }

  #filebrowser-loading-page .team-tile .circles {
    display: flex;
    flex-direction: row;
  }

  #filebrowser-loading-page .team-tile .circle {
    top: 0;
    left: 0;
    width: 24px;
    height: 24px;
    margin-right: 8px;
    margin-top: 22px;
  }

  #filebrowser-loading-page .public-header {
    background-color: #f0f0f0;
    width: 100%;
    height: 240px;
    margin-bottom: 80px;
  }

  #filebrowser-loading-page .profile-header {
    background-color: #f0f0f0;
    width: 100%;
    height: 64px;
  }

  #filebrowser-loading-page .profile-grid {
    padding: 32px;
    display: grid;
    grid-template-columns: 1fr 24px 1fr .75fr;
    align-items: end;
  }

  #filebrowser-loading-page .profile-grid .row {
    margin-top: 24px;
  }

  #filebrowser-loading-page .profile-grid div:nth-child(4n+1) { width: 148px; }
  #filebrowser-loading-page .profile-grid div:nth-child(4n+3) { width: 56px; }
  #filebrowser-loading-page .profile-grid div:nth-child(4n+4) { width: 99px; }

  #filebrowser-loading-page .profile-grid div:nth-child(1) { width: 61px; margin-top: 0; }

  #filebrowser-loading-page .profile-grid div:nth-child(5) { width: 61px; margin-top: 32px; }
  #filebrowser-loading-page .profile-grid div:nth-child(7) { width: 69px; }
  #filebrowser-loading-page .profile-grid div:nth-child(8) { width: 51px; }

  #filebrowser-loading-page .profile-grid div:nth-child(9) { margin-top: 36px; }
  #filebrowser-loading-page .profile-grid div:nth-child(11) { width: 69px; }
  #filebrowser-loading-page .profile-grid div:nth-child(12) { width: 72px; }

  #filebrowser-loading-page .profile-grid div:nth-child(25),
  #filebrowser-loading-page .profile-grid div:nth-child(27),
  #filebrowser-loading-page .profile-grid div:nth-child(28) { opacity: .8; }

  #filebrowser-loading-page .profile-grid div:nth-child(29),
  #filebrowser-loading-page .profile-grid div:nth-child(31),
  #filebrowser-loading-page .profile-grid div:nth-child(32) { opacity: .4; }

  @media(max-width: 1000px) {
    #filebrowser-loading-page .profile-grid {
      grid-template-columns: 1fr;
    }

    #filebrowser-loading-page .profile-grid div:nth-child(5),
    #filebrowser-loading-page .profile-grid div:nth-child(6),
    #filebrowser-loading-page .profile-grid div:nth-child(7),
    #filebrowser-loading-page .profile-grid div:nth-child(8),
    #filebrowser-loading-page .profile-grid div:nth-child(4n+2),
    #filebrowser-loading-page .profile-grid div:nth-child(4n+3),
    #filebrowser-loading-page .profile-grid div:nth-child(4n+4) { display: none; }
  }

  #filebrowser-loading-page .project-grid {
    padding-left: 32px;
    display: grid;
    grid-row-gap: 22px;
  }

  #filebrowser-loading-page .project-grid .card {
    border: 1px solid rgba(0, 0, 0, .1);
    border-radius: 4px;
    box-sizing: border-box;
    height: 178px;
    display: flex;
  }

  #filebrowser-loading-page .project-grid .card:nth-child(3) { opacity: .8; }
  #filebrowser-loading-page .project-grid .card:nth-child(4) { opacity: .4; }

  #filebrowser-loading-page .project-grid .card .left {
    width: 196px;
    margin: 16px;
  }

  #filebrowser-loading-page .project-grid .card .right {
    flex: 1 1;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    overflow: hidden;
    margin: 16px 0;
  }

  #filebrowser-loading-page .project-grid .card .left .row:nth-child(1) { width: 107px; }
  #filebrowser-loading-page .project-grid .card .left .row:nth-child(2) { width: 164px; margin-top: 12px; }
  #filebrowser-loading-page .project-grid .card .left .row:nth-child(3) { width: 145px; margin-top: 8px; }
  #filebrowser-loading-page .project-grid .card .left .row:nth-child(4) { width: 158px; margin-top: 8px; }

  #filebrowser-loading-page .project-grid .card .right .row {
    height: 100%;
    flex: 1 1 196px;
    margin-right: 16px;
    border-radius: 6px;
  }

  #filebrowser-loading-page .right-column {
    flex: 0 0 304px;
    margin-right: 16px;
    margin-top: 16px;
    box-sizing: border-box;
    padding-left: 32px;
  }

  #filebrowser-loading-page .right-column .row:nth-child(1) {
    margin-top: 16px;
    width: 120px;
  }
  #filebrowser-loading-page .right-column .row:nth-child(2) {
    margin-top: 18px;
    width: 272px;
  }
  #filebrowser-loading-page .right-column .row:nth-child(3) {
    margin-top: 8px;
    width: 248px;
  }
  #filebrowser-loading-page .right-column .row:nth-child(4) {
    margin-top: 8px;
    width: 272px;
  }
  #filebrowser-loading-page .right-column .row:nth-child(5) {
    margin-top: 8px;
    width: 256px;
  }
  #filebrowser-loading-page .right-column .row:nth-child(6) {
    margin-top: 8px;
    width: 200px;
  }
  #filebrowser-loading-page .right-column .row:nth-child(7) {
    margin-top: 35px;
    width: 88px;
  }
  #filebrowser-loading-page .right-column .row:nth-child(8) {
    margin-top: 22px;
    margin-left: 51px;
    width: 88px;
    opacity: .8;
  }
  #filebrowser-loading-page .right-column .row:nth-child(9) {
    margin-top: 18px;
    margin-left: 51px;
    width: 88px;
    opacity: .4;
  }

  #filebrowser-loading-page .public-left-column {
    padding: 0 0 32px 32px;
    width: 320px;
  }

  #filebrowser-loading-page .public-left-column .row {
    margin-top: 8px;
  }

  #filebrowser-loading-page .public-left-column .row:nth-child(1) {
    width: 120px;
    margin-top: 0;
  }
  #filebrowser-loading-page .public-left-column .row:nth-child(2) {
    width: 272px;
    margin-top: 18px;
  }
  #filebrowser-loading-page .public-left-column .row:nth-child(3) {
    width: 248px;
  }
  #filebrowser-loading-page .public-left-column .row:nth-child(4) {
    width: 272px;
  }
  #filebrowser-loading-page .public-left-column .row:nth-child(5) {
    width: 256px;
    opacity: .8;
  }
  #filebrowser-loading-page .public-left-column .row:nth-child(6) {
    width: 200px;
    opacity: .4;
  }

  /*
  Note: Make sure any changes here are also duplicated in the fullscreen progress bar
  (.progressBar in progress_bar.css)
  */
  #filebrowser-loading-progress-bar {
    height: 5px;
      background: #18A0FB;
    position: absolute;
    left: 0;
    animation: filebrowserloadingProgressBar 10s cubic-bezier(.08,.8,.1,1) forwards;
  }

  @keyframes filebrowserloadingProgressBar {
    from { width: 0; }
    to { width: 100%; }
  }


  @media (max-width: 645px) {
    .filebrowser-loading-sidebar {
      display: none;
    }

    #filebrowser-loading-page .page {
      margin-left: 0;
      width: 100%;
    }

    #filebrowser-loading-page .public-header {
      height: 120px;
    }

    #filebrowser-loading-page .file-grid {
      grid-template-columns: 1fr;
      max-width: 400px;
      margin: 0 auto;
      align-self: center;
    }
  }

</style>


      <meta name="mobile-web-app-capable" content="yes">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    
    <meta property="og:title" content="Figma">
    <meta property="og:site_name" content="Figma">

    


<link rel="icon" sizes="192x192" href="https://static.figma.com/app/icon/1/icon-192.png">
<link rel="icon" sizes="128x128" href="https://static.figma.com/app/icon/1/icon-128.png">

<link rel="icon" type="image/png" href="https://static.figma.com/app/icon/1/favicon.png">
<!--[if IE]><link rel="shortcut icon" href="https://static.figma.com/app/icon/1/favicon.ico" type="image/vnd.microsoft.icon" /><![endif]-->
<link rel="icon" sizes="any" type="image/svg+xml" href="https://static.figma.com/app/icon/1/favicon.svg">

<link rel="apple-touch-icon" sizes="76x76" href="https://static.figma.com/app/icon/1/touch-76.png">
<link rel="apple-touch-icon" sizes="120x120" href="https://static.figma.com/app/icon/1/touch-120.png">
<link rel="apple-touch-icon" sizes="152x152" href="https://static.figma.com/app/icon/1/touch-152.png">
<link rel="apple-touch-icon" sizes="167x167" href="https://static.figma.com/app/icon/1/touch-167.png">
<link rel="apple-touch-icon" sizes="180x180" href="https://static.figma.com/app/icon/1/touch-180.png">


      <link href="https://www.figma.com/figbuild-artifacts/figma_app.af1d40a8a3052d1d02bf184af8a66dd6.min.css.br" rel="stylesheet">

        <link rel="preload" href="https://static.figma.com/webfont/1/Inter-Regular.woff2?v=3.10" as="font" crossorigin="anonymous">
        <link rel="preload" href="https://static.figma.com/webfont/1/Inter-Italic.woff2?v=3.10" as="font" crossorigin="anonymous">
        <link rel="preload" href="https://static.figma.com/webfont/1/Inter-Medium.woff2?v=3.10" as="font" crossorigin="anonymous">
        <link rel="preload" href="https://static.figma.com/webfont/1/Inter-MediumItalic.woff2?v=3.10" as="font" crossorigin="anonymous">
        <link rel="preload" href="https://static.figma.com/webfont/1/Inter-SemiBold.woff2?v=3.10" as="font" crossorigin="anonymous">
        <link rel="preload" href="https://static.figma.com/webfont/1/Inter-SemiBoldItalic.woff2?v=3.10" as="font" crossorigin="anonymous">
        <link rel="preload" href="https://static.figma.com/webfont/1/DSEG7Classic-Italic-Custom2.woff2" as="font" crossorigin="anonymous">

  <script type="text/javascript" async="" nonce="" crossorigin="anonymous" src="https://static.figma.com/fullscreen/6ec1792e764602e75d392be212aaf69990b23434/compiled_wasm.js.br"></script><script type="text/javascript" async="" nonce="" crossorigin="anonymous" src="https://static.figma.com/fullscreen/d26937d75bdf683235c614a9a57cac3ca4c2a46a/import.shim.js.br"></script></head>
  <body class="feature_flag_figjam_plugins_validation feature_flag_voice_enabled">
      <div style="position: fixed; top: -1000px; left: -1000px;">
        <div aria-hidden="true" id="font-ui-400-normal">a</div>
        <div aria-hidden="true" id="font-ui-400-italic">a</div>
        <div aria-hidden="true" id="font-ui-500-normal">a</div>
        <div aria-hidden="true" id="font-ui-500-italic">a</div>
        <div aria-hidden="true" id="font-ui-600-normal">a</div>
        <div aria-hidden="true" id="font-ui-600-italic">a</div>

        <div aria-hidden="true" id="font-ui-400-normal-white">a</div>
      </div>

    <div id="react-page"><div class="in_app_page--app--234Z6 in_app_page--appFont--3IVZv"><div class="in_app_page--content--2V_He"><div><div class="navbar--navbarContainer--13Uu5"><div><div class="navbar--leftInnerNav--20Ei9 navbar--leftNav--1LTAM"><div class="action--enabled--16Cku action--root--1ClVW toolbar_styles--enabledButton--2cWGq navbar--workspaceNav--3iBYr navbar--navbarAction--3J65x chevron--chevronContainer--3xT09"><div class="workspace_icon--container--1MXBZ navbar--workspaceIcon--2kNdU"><span class="svg-container"><svg class="svg" width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M10 11c0-1.657 1.343-3 3-3h5c1.657 0 3 1.343 3 3 0 1.043-.533 1.963-1.341 2.5.808.537 1.341 1.457 1.341 2.5 0 1.657-1.343 3-3 3-.768 0-1.47-.289-2-.764V21c0 1.657-1.343 3-3 3-1.657 0-3-1.343-3-3 0-1.044.533-1.962 1.341-2.5C10.533 17.962 10 17.044 10 16c0-1.043.533-1.963 1.341-2.5C10.533 12.963 10 12.043 10 11zm3 2c-1.105 0-2-.895-2-2 0-1.105.895-2 2-2h2v4h-2zm2 1h-2c-1.105 0-2 .895-2 2 0 1.105.895 2 2 2h2v-4zm0 5h-2c-1.105 0-2 .895-2 2 0 1.105.895 2 2 2 1.105 0 2-.895 2-2v-2zm3-5c-1.105 0-2 .895-2 2 0 1.105.895 2 2 2 1.105 0 2-.895 2-2 0-1.105-.895-2-2-2zm0-1c1.105 0 2-.895 2-2 0-1.105-.895-2-2-2h-2v4h2z" fill-rule="evenodd" fill-opacity="1" fill="#000" stroke="none"></path></svg></span></div><div class="navbar--workspaceName--ZNOS1"><div class="navbar--workspaceTitleSmaller--1jIB2 navbar--_workspaceTitle--34oCv navbar--ellipsis--3SO1g ellipsis--ellipsis--1RWY6 text--fontNeg12--oxUtr text--_fontBase--YWDo0 text--_whiteText--2PkdM" data-testid="navbar-workspace-title"><span class="navbar--ellipsis--3SO1g ellipsis--ellipsis--1RWY6">KUSHAGRA PATIDAR</span></div><div class="navbar--workspaceSubtitle--GGsAf text--fontNeg9--jzHz0 text--_fontBase--YWDo0 text--_whiteText--2PkdM navbar--ellipsis--3SO1g ellipsis--ellipsis--1RWY6">kushagra24ai027@satiengg.in</div></div><div class="navbar--chevronContainer--iFE72"><div class="chevron--chevronContainer--3xT09  " data-tooltip-type="text"><span class="svg-container chevron--svgChevron--ttrRg "><svg class="svg" width="8" height="7" viewBox="0 0 8 7" xmlns="http://www.w3.org/2000/svg"><path d="M3.646 5.354l-3-3 .708-.708L4 4.293l2.646-2.647.708.708-3 3L4 5.707l-.354-.353z" fill-rule="evenodd" fill-opacity="1" fill="#fff" stroke="none"></path></svg></span></div></div></div></div><div data-tooltip-type="text" data-tooltip-show-below="true" data-tooltip-timeout-delay="50" data-tooltip-max-width="300"><div class="action--disabled--2gd1h action--root--1ClVW toolbar_styles--disabledButton--AaXxQ navbar--searchAction--13qGD navbar--navbarAction--3J65x"><div><form><div class=" search--expandingSearchBoxContainer--2Xgv_ search--_expandingSearchBoxContainerBase--2L720 search--searchContainer--U7vsO"><span class="svg-container search--searchIconBrowseIA--3M-Ke search--searchIcon--2srT2"><svg class="svg" width="15" height="15" viewBox="0 0 15 15" xmlns="http://www.w3.org/2000/svg"><path d="M14.146 14.854l.708-.708-4.272-4.272C11.466 8.83 12 7.477 12 6c0-3.314-2.686-6-6-6-3.314 0-6 2.686-6 6 0 3.314 2.686 6 6 6 1.477 0 2.83-.534 3.874-1.418l4.272 4.272zM11 6c0 2.761-2.239 5-5 5-2.761 0-5-2.239-5-5 0-2.761 2.239-5 5-5 2.761 0 5 2.239 5 5z" fill-rule="nonzero" fill-opacity="1" fill="#000" stroke="none"></path></svg></span><input placeholder="Search " class="search--searchInput--2JmjM text--fontPos13--1DoEt text--_fontBase--YWDo0 lazy_input--lazyInput--2kTZE" spellcheck="false" type="text" value="" style="width: 50px;"><div class="search--hiddenPlaceholderTextBrowseIA--1sa4C search--hiddenPlaceholderText--3Spiy text--fontNeg13--2PnkS text--_fontBase--YWDo0 text--_whiteText--2PkdM">Search </div></div></form></div></div></div></div><div><div data-onboarding-key="ACCOUNT_SWITCHING_NOTIFICATION_ONBOARDING_KEY" data-tooltip-type="text" data-tooltip-show-below="true" data-tooltip-timeout-delay="50" data-tooltip-max-width="300"><div class="navbar--mainRedDotAndTopBarActionContainer--1fBdu red_dot--redDotAndIconContainer--2dklW"><div class="action--enabled--16Cku action--root--1ClVW toolbar_styles--enabledButton--2cWGq navbar--navbarAction--3J65x"><span class="svg-container"><svg class="svg" width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M20 14v3c0 .768.289 1.47.764 2h-9.528c.475-.53.764-1.232.764-2v-3c0-2.21 1.79-4 4-4 2.21 0 4 1.79 4 4zm1 0v3c0 1.105.895 2 2 2v1H9v-1c1.105 0 2-.895 2-2v-3c0-2.761 2.239-5 5-5 2.761 0 5 2.239 5 5zm-5 9c-1.105 0-2-.895-2-2h-1c0 1.657 1.343 3 3 3 1.657 0 3-1.343 3-3h-1c0 1.105-.895 2-2 2z" fill-rule="evenodd" fill-opacity="1" fill="#000" stroke="none"></path></svg></span></div></div></div><div class="action--enabled--16Cku action--root--1ClVW toolbar_styles--enabledButton--2cWGq navbar--profileAction--3Jn4_ navbar--navbarAction--3J65x chevron--chevronContainer--3xT09" data-testid="ProfileButton"><div class="workspace_icon--container--1MXBZ "><div class="workspace_icon--iconContainer--1gWYz"><span class="avatar--avatar--rj2Q0 avatar--circle--2J3z6  " style="display: flex; justify-content: center; color: white; background-color: rgb(199, 185, 255); width: 24px; height: 24px; line-height: 24px; font-size: 12px;">K</span><div class="workspace_icon--shadow--2JNMX"></div></div></div><div class="navbar--chevronContainer--iFE72" data-onboarding-key="FILE_BROWSER_WORKSPACE_SWITCHER"><div class="chevron--chevronContainer--3xT09  " data-tooltip-type="text"><span class="svg-container chevron--svgChevron--ttrRg "><svg class="svg" width="8" height="7" viewBox="0 0 8 7" xmlns="http://www.w3.org/2000/svg"><path d="M3.646 5.354l-3-3 .708-.708L4 4.293l2.646-2.647.708.708-3 3L4 5.707l-.354-.353z" fill-rule="evenodd" fill-opacity="1" fill="#fff" stroke="none"></path></svg></span></div></div></div></div></div><div class="sidebar--navDefault--1zbCB"><div class="scroll_container--clipContainer--2PG4d sidebar--sidebarScrollContainer--3CVrq js-fullscreen-wheel-event-capture"><div class="scroll_container--scrollContainer--1eEK2"><div class="scroll_container--innerScrollContainer--21gfN "><div class="sidebar--navContent--sh3Ue"><div class="sidebar--section--1UxqU"><a class="recent_files_link--recentFiles--g505D sidebar--sidebarSection--3XvYF text--fontPos11--RSei3 text--_fontBase--YWDo0"><span class="svg-container recent_files_link--recentFilesIcon--AxFdS sidebar--icon--1Z2rN"><svg class="svg" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M8 16c4.418 0 8-3.582 8-8 0-4.418-3.582-8-8-8-4.418 0-8 3.582-8 8 0 4.418 3.582 8 8 8zm0-1c-3.866 0-7-3.134-7-7 0-3.866 3.134-7 7-7 3.866 0 7 3.134 7 7 0 3.866-3.134 7-7 7zM8 4H7v5h5V8H8V4z" fill-rule="nonzero" fill-opacity="1" fill="#000" stroke="none"></path></svg></span><span class="recent_files_link--recentFilesName--38Ivv sidebar--sectionName--eII3k sidebar--sectionText--31Nhy sidebar--sectionContent--2dhhM ellipsis--ellipsis--1RWY6">Recent</span></a><div data-onboarding-key="DRAFT_FOLDER_LINK_ONBOARDING_KEY"><div class="folder_link--folderLink--pgMyD sidebar--folder--OE9-f sidebar--sidebarSection--3XvYF text--fontPos11--RSei3 text--_fontBase--YWDo0" draggable="false"><div class="folder_link--tileBorder--1s4e5"></div><span class="svg-container folder_link--draftsIcon--vocV3 sidebar--icon--1Z2rN"><svg class="svg" width="12" height="16" viewBox="0 0 12 16" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h7.707l.147.146 4 4 .146.147V15H0V0zm1 1v13h10V5H7V1H1zm7 .707L10.293 4H8V1.707z" fill-rule="evenodd" fill-opacity="1" fill="#000" stroke="none"></path></svg></span><span class="folder_link--draftsName--27zLb folder_link--folderName--2Eh16 sidebar--sectionName--eII3k sidebar--sectionText--31Nhy sidebar--sectionContent--2dhhM ellipsis--ellipsis--1RWY6">Drafts</span></div><div class="folder_link--dragImage--3W5Cd"></div></div></div><div class="sidebar--section--1UxqU"><div class="sidebar--dividerSmall--2P1CR sidebar--divider--2X5fS"></div><a href="/community" class="community_hub_link--communitySection--10KFH sidebar--sidebarSection--3XvYF text--fontPos11--RSei3 text--_fontBase--YWDo0" data-onboarding-key="community-tab"><span class="svg-container community_hub_link--icon--30LMn sidebar--icon--1Z2rN"><svg class="svg" width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M8.518 16c.219 3.104 2.46 5.649 5.415 6.324-.81-1.325-1.365-3.646-1.427-6.324H8.518zm6.982 7.5c-4.418 0-8-3.582-8-8 0-4.418 3.582-8 8-8 4.418 0 8 3.582 8 8 0 4.418-3.582 8-8 8zM13.934 8.676c-2.955.675-5.197 3.22-5.416 6.324h3.988c.062-2.678.618-5 1.428-6.324zm3.133 0c2.954.675 5.196 3.22 5.415 6.324h-3.988c-.062-2.678-.618-5-1.427-6.324zM22.482 16c-.219 3.104-2.46 5.649-5.415 6.324.81-1.325 1.365-3.646 1.427-6.324h3.988zm-5.797 4.806c.452-1.206.763-2.891.809-4.806h-3.988c.046 1.915.357 3.6.809 4.806.247.658.517 1.121.766 1.402.25.282.394.292.419.292.025 0 .17-.01.42-.292.248-.28.518-.744.765-1.402zm-2.37-10.612c-.452 1.205-.762 2.891-.809 4.806h3.988c-.046-1.915-.357-3.6-.809-4.806-.247-.658-.517-1.121-.765-1.402-.25-.282-.395-.292-.42-.292-.025 0-.17.01-.42.292-.248.28-.518.744-.765 1.402z" fill-rule="evenodd" fill-opacity="1" fill="#000" stroke="none"></path></svg></span><span class="community_hub_link--sectionName--3mjGP sidebar--sectionName--eII3k sidebar--sectionText--31Nhy sidebar--sectionContent--2dhhM ellipsis--ellipsis--1RWY6">Community<span class="badge--badgeSmall--tBqry text--fontPos9--27Y9u text--_fontBase--YWDo0 badge--boldGreen--3n3o_ community_hub_link--communityBetaTag--eeCdZ">Beta</span></span><span class="svg-container community_hub_link--communityArrow--16EEA"><svg class="svg" width="14" height="10" viewBox="0 0 14 10" xmlns="http://www.w3.org/2000/svg"><path d="M0 4.75h11.29l-3.4-3.388.706-.709 4.612 4.597-4.612 4.597-.706-.709 3.4-3.388H0v-1z" fill-rule="evenodd" fill-opacity=".8" fill="#000" stroke="none"></path></svg></span></a></div><div class="sidebar--section--1UxqU"><div class="upgrade_section--divider--2MVtg sidebar--dividerSmall--2P1CR sidebar--divider--2X5fS"></div><div class="upgrade_section--upgradeMainSection--1k31b sidebar--sidebarSection--3XvYF text--fontPos11--RSei3 text--_fontBase--YWDo0"><span class=" upgrade_section--icon--1PFR0 sidebar--icon--1Z2rN"><svg class="svg" width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M16 23c3.866 0 7-3.134 7-7 0-3.866-3.134-7-7-7-3.866 0-7 3.134-7 7 0 3.866 3.134 7 7 7zm0 1c4.418 0 8-3.582 8-8 0-4.418-3.582-8-8-8-4.418 0-8 3.582-8 8 0 4.418 3.582 8 8 8zm0-12.1l-.354.354-3 3 .708.707 2.146-2.147v6.293h1v-6.293l2.146 2.147.708-.707-3-3L16 11.9z" fill-rule="evenodd" fill-opacity=".8" fill="#000" stroke="none"></path></svg></span><div class="upgrade_section--upgradeMainText--1uTu- sidebar--sectionName--eII3k sidebar--sectionText--31Nhy sidebar--sectionContent--2dhhM ellipsis--ellipsis--1RWY6">Upgrade plan for unlimited design files in teams</div></div><div class="upgrade_section--upgradeSubSection--3IABk upgrade_section--upgradeMainSection--1k31b sidebar--sidebarSection--3XvYF text--fontPos11--RSei3 text--_fontBase--YWDo0"><button type="button" class="basic_form--btn--3A-Ju ellipsis--ellipsis--1RWY6 text--fontPos11--RSei3 text--_fontBase--YWDo0 upgrade_section--upgradeButton--1R-EG" data-testid="upgrade-button">Upgrade</button></div></div><div><div class="" draggable="true"><div class="sidebar--dividerSmall--2P1CR sidebar--divider--2X5fS"></div><div><div class="nav_section--section--zokZk sidebar--section--1UxqU"><div data-onboarding-key="TEAM_FILES_ONBOARDING_KEY"><div class="team_link--selectedTeam--1whFT sidebar--selected--BMSeP team_link--team--1-tA5 sidebar--sidebarSection--3XvYF text--fontPos11--RSei3 text--_fontBase--YWDo0"><div class="team_link--teamDetails--2DmNG"><div class="team_link--tileBorder--3FU3b"></div><div class="team_link--icon--hbbyD sidebar--icon--1Z2rN"><span class="avatar--avatar--rj2Q0 avatar--square--2vQe3  " style="display: flex; justify-content: center; color: white; background-color: rgb(255, 133, 119); width: 14px; height: 14px; line-height: 14px; font-size: 7px;"></span></div><div class="team_link--teamName--26rIb sidebar--sectionHeaderName--17dPf sidebar--sectionName--eII3k sidebar--sectionText--31Nhy sidebar--sectionContent--2dhhM ellipsis--ellipsis--1RWY6">Web Squad</div></div></div></div><div class="nav_section--orderedFoldersEmpty--1TlFD nav_section--orderedFolders--2rM_R"><div class="nav_section--folderSeparatorBefore--uM190"><div class="nav_section--folderSeparatorOff--_N9sh nav_section--sectionText--1_2Fk sidebar--sectionText--31Nhy sidebar--sectionContent--2dhhM ellipsis--ellipsis--1RWY6"></div></div><div class="nav_section--emptyFavFolderSection--1A5CV sidebar--folder--OE9-f sidebar--sidebarSection--3XvYF text--fontPos11--RSei3 text--_fontBase--YWDo0"><span class="nav_section--iconEmpty--1RYhu sidebar--iconEmpty--3KvV3 sidebar--icon--1Z2rN"></span><div class="nav_section--emptyFavFolder--3-ln6 sidebar--sectionName--eII3k sidebar--sectionText--31Nhy sidebar--sectionContent--2dhhM ellipsis--ellipsis--1RWY6">Add a project to your favorites to see it here</div></div><div class="nav_section--folderSeparatorAfter--uW5iu"><div class="nav_section--folderSeparatorOff--_N9sh nav_section--sectionText--1_2Fk sidebar--sectionText--31Nhy sidebar--sectionContent--2dhhM ellipsis--ellipsis--1RWY6"></div></div></div></div></div></div><div class="sidebar--dragImage--1PcuK"></div></div><div></div><div class="sidebar--dividerSmall--2P1CR sidebar--divider--2X5fS"></div><div class="new_team_link--createNewTeamLink--3VPWN" data-onboarding-key="create-team-link"><div class="new_team_link--navLink--x86P_ sidebar--sidebarSection--3XvYF text--fontPos11--RSei3 text--_fontBase--YWDo0"><div class="new_team_link--buttonHover--2hWLS new_team_link--_button--3tF5L"><div data-onboarding-key="new-team-icon" class="new_team_link--icon--1yQ1_ sidebar--icon--1Z2rN"><span class="svg-container"><svg class="svg" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M15 8V7H9V1H8v6H2v1h6v6h1V8h6z" fill-rule="nonzero" fill-opacity="1" fill="#000" stroke="none"></path></svg></span></div><div class="new_team_link--name--37ECQ sidebar--sectionName--eII3k sidebar--sectionText--31Nhy sidebar--sectionContent--2dhhM ellipsis--ellipsis--1RWY6">Create new team</div></div></div></div></div><div style="display: none; height: 0px;"></div></div></div></div></div><div class="file_browser_view--fileBrowserPageViewContainer--1olui"><div class="mobile_tool_bar--mobileActionsContainerWithoutBoxShadow--1mkcZ mobile_tool_bar--mobileActionsContainer--2-7qI"><div class="mobile_tool_bar--toolBarMobileLeftSide--5qodq"><span tabindex="0" class=" raw_components--iconButtonEnabled--1oUUU raw_components--_iconButton--353Le" aria-label="Show navigation"><svg class="svg" width="18" height="18" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg"><path d="M16 13H2v1h14v-1zm0-5H2v1h14V8zm0-5H2v1h14V3z" fill-rule="nonzero" fill-opacity="1" fill="#000" stroke="none"></path></svg></span></div></div><div class="mobile_tool_bar--mobileActionsSpacerContainer--UUg5n"></div><div class="desktop_tool_bar--toolBarSpacerContainer--3wF93"><div class="desktop_tool_bar--pageViewToolBarContainer--2k8we desktop_tool_bar--toolBarContainer--VnCpw"><div class="desktop_tool_bar--toolBarLeftSide--3IZKD text--fontPos13--1DoEt text--_fontBase--YWDo0"><div class="tab--base--vEslZ text--fontPos13--1DoEt text--_fontBase--YWDo0 desktop_tool_bar--toolBarTabContentBase--3IywG tab--selected--2mpPj "><span class="desktop_tool_bar--toolBarTabContent--3Nltd ellipsis--ellipsis--1RWY6">Web Squad</span></div><div class="tab--base--vEslZ text--fontPos13--1DoEt text--_fontBase--YWDo0 desktop_tool_bar--toolBarTabContentBase--3IywG tab--unselected--2T1WZ "><span class="desktop_tool_bar--toolBarTabContent--3Nltd ellipsis--ellipsis--1RWY6">Members</span></div></div><div class="desktop_tool_bar--toolBarRightSide--1Azft"><button class="desktop_tool_bar--toolBarButton--PIG7r text--fontPos11--RSei3 text--_fontBase--YWDo0 ">New project</button></div></div></div><div class="file_browser_page_view--mobileToolBarSpacer--3S451"></div><div></div><div class="file_browser_page_view--container--88Ioi"><div class="file_browser_page_view--metaContainer--33Uas"><div class="team_overview--avatar--2nJSS"><span class="avatar--avatar--rj2Q0 avatar--square--2vQe3  " style="display: flex; justify-content: center; color: white; background-color: rgb(255, 133, 119); width: 32px; height: 32px; line-height: 32px; font-size: 16px;">W</span></div><div class="team_overview--metaTeamName--29dvj org_home_view_meta_content--orgName--3XeZo text--fontPos18--3M8-H text--_fontBase--YWDo0" data-testid="team-name">Web Squad</div><div class="team_overview--teamType--24-Dz org_home_view_meta_content--organization--3F2nf text--fontPos11--RSei3 text--_fontBase--YWDo0" data-testid="team-type">Starter team</div><div class="team_overview--sidebarDivider--2GyE2 upgrade_section--sidebarDivider--kuhdr"></div><div class="team_overview--teamMembersContainer--23Hqt org_home_view_meta_content--orgMembersContainer--1fq6R"><div><div class="members_preview--header--1hW2T text--fontPos13--1DoEt text--_fontBase--YWDo0">Members</div><div class="avatar--avatarWithHandle--2G2Vu avatar--clickableAvatarWithHandle--1l4mS  members_preview--member--Zj9XO text--fontPos13--1DoEt text--_fontBase--YWDo0" data-tooltip-proxy-element-id="avatar_1019473611201361470_tooltip_proxy"><div id="avatar_1019473611201361470_tooltip_proxy" data-tooltip-type="text"><span class="avatar--avatar--rj2Q0 avatar--circle--2J3z6  " style="display: flex; justify-content: center; color: white; background-color: rgb(199, 185, 255); width: 24px; height: 24px; line-height: 24px; font-size: 12px;">K</span></div><div class="avatar--info--6fmV-"><div class="avatar--handleRow--3gz7_ avatar--avatarWithHandle--2G2Vu "><span class="avatar--handle--fICEU">KUSHAGRA PATIDAR</span><span class="avatar--isMe--1tfH3">(You)</span></div></div><span class="members_preview--leaveLink--dEOhD text--fontPos13--1DoEt text--_fontBase--YWDo0 blue_link--blueLink--22X56">Leave</span></div><div class="avatar--avatarWithHandle--2G2Vu avatar--clickableAvatarWithHandle--1l4mS  members_preview--member--Zj9XO text--fontPos13--1DoEt text--_fontBase--YWDo0" data-tooltip-proxy-element-id="avatar_1014075699925451805_tooltip_proxy"><div id="avatar_1014075699925451805_tooltip_proxy" data-tooltip-type="text"><span class="avatar--avatar--rj2Q0 avatar--circle--2J3z6  " style="display: flex; justify-content: center; color: white; background-color: rgb(85, 81, 255); width: 24px; height: 24px; line-height: 24px; font-size: 12px;">H</span></div><div class="avatar--info--6fmV-"><div class="avatar--handleRow--3gz7_ avatar--avatarWithHandle--2G2Vu "><span class="avatar--handle--fICEU">Himanshu Agnihotri</span></div></div></div></div><div class="team_members_preview--inviteMembersContainer--3P0C7"><span class="svg-container team_members_preview--inviteIcon--2-PRK members_preview--teamIcon--30B3O" data-onboarding-key="starter-team-members-preview"><svg class="svg" width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path d="M5 5V0h1v5h5v1H6v5H5V6H0V5h5z" fill-rule="nonzero" fill-opacity="1" fill="#000" stroke="none"></path></svg></span><span class="team_members_preview--inviteText--1TyuT text--fontPos13--1DoEt text--_fontBase--YWDo0">Invite members</span></div></div><div class="team_overview--sidebarDivider--2GyE2 upgrade_section--sidebarDivider--kuhdr"></div><div class="starter_team_overview--container--2SDzK text--fontPos13--1DoEt text--_fontBase--YWDo0"><div class="starter_team_overview--header--285Vg text--fontPos13--1DoEt text--_fontBase--YWDo0">Starter team overview</div><div class="starter_team_overview--detailsWithFigjam--2ZwQ4"><div><span class="svg-container starter_team_overview--detailsWithFigjamIcon--3gQsH"><svg class="svg" width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M20.374 23.207c.39.39 1.024.39 1.415 0l1.414-1.414c.39-.39.39-1.024 0-1.414l-9.414-9.415-2.829 2.829-.707-.707 2.829-2.829-1.272-1.27-3.535-.708.707 3.536 11.392 11.392zM8.062 7.217l4.241.848L23.91 19.672c.781.78.781 2.047 0 2.828l-1.414 1.414c-.781.781-2.048.781-2.829 0L8.061 12.308l-.849-4.241L7 7.004l1.062.213z" fill-rule="evenodd" fill-opacity=".8" fill="#000" stroke="none"></path></svg></span><span>Unlimited FigJam files (during beta)</span></div><div><span class="svg-container starter_team_overview--detailsWithFigjamIcon--3gQsH"><svg class="svg" width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M17.122 11.64l-.012-.003-6.666-1.9 4.91 4.91c.195-.095.414-.147.646-.147.828 0 1.5.672 1.5 1.5 0 .828-.672 1.5-1.5 1.5-.828 0-1.5-.672-1.5-1.5 0-.232.053-.45.146-.647L9.743 10.45l1.832 6.39.01.037.008.037C12.015 18.961 13.829 20.5 16 20.5c.494 0 .968-.08 1.411-.225l.585-.193.435.435 1.847 1.847 2.122-2.121-1.865-1.865-.43-.43.184-.58c.137-.43.211-.89.211-1.368 0-2.093-1.43-3.854-3.366-4.356l-.012-.003zm5.985 7.895l.707.708-.707.707-2.122 2.121-.707.707-.707-.707-1.847-1.847c-.542.18-1.122.276-1.724.276-2.655 0-4.871-1.882-5.387-4.384L8.325 9.132 8 8l1.133.323 8.252 2.353C19.752 11.29 21.5 13.44 21.5 16c0 .582-.09 1.144-.258 1.67l1.865 1.865z" fill-rule="evenodd" fill-opacity=".8" fill="#000" stroke="none"></path></svg></span><span>1 of 3 Figma design files used</span></div><div><span class="svg-container starter_team_overview--detailsWithFigjamIcon--3gQsH"><svg class="svg" width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M9 10h7v2H9v-2zm-1 2V9h9v3h7v11H8V12zm9 1H9v9h14v-9h-6z" fill-rule="evenodd" fill-opacity=".8" fill="#000" stroke="none"></path></svg></span><span>1 of 1 project used</span></div><div><span class="svg-container starter_team_overview--detailsWithFigjamIcon--3gQsH"><svg class="svg" width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M15.373 22h1.258c.28-.32.616-.597.995-.819 1.479-.862 4.005-.909 5.386.109H24.5v-9.2c0 0-.797-2.25-4.42-2.25-1.875 0-2.902.602-3.456 1.184-.389.407-.545.804-.6.976h-.049c-.054-.172-.21-.57-.599-.976-.554-.582-1.581-1.184-3.456-1.184-3.623 0-4.42 2.25-4.42 2.25v9.19h1.488c1.382-1.019 3.91-.97 5.388-.105.38.223.717.502.997.825zm1.127-9.711v8.457c.195-.157.403-.3.622-.428.927-.541 2.115-.796 3.241-.787 1.006.008 2.081.227 2.952.759h.185v-7.973l-.03-.05c-.086-.138-.236-.339-.474-.545-.461-.397-1.33-.882-2.916-.882-1.586 0-2.34.483-2.694.835-.189.186-.296.367-.354.49-.029.061-.045.108-.052.131l-.005.017.001-.006.002-.008v-.005l.001-.002v-.002l-.005-.001H16.5zm-1 0h-.475l-.005.001v.002l.001.002.001.005.002.008.001.006c0 .001 0-.005-.005-.017-.007-.023-.024-.07-.053-.131-.057-.123-.164-.303-.353-.49-.354-.352-1.108-.835-2.694-.835-1.585 0-2.455.485-2.916.882-.238.206-.388.407-.474.545l-.03.05v7.963h.185c.872-.533 1.948-.752 2.954-.759 1.128-.008 2.316.249 3.243.792.217.127.424.27.618.426v-8.45z" fill-rule="evenodd" fill-opacity=".45" fill="#000" stroke="none"></path></svg></span><span class="starter_team_overview--customLibrariesText--2g50q">Custom libraries (Professional only)</span></div></div></div><div class="upgrade_section--sidebarDivider--kuhdr"></div><div class="upgrade_section--upsellDescription--NOvph org_home_view_meta_content--description--2Gs02 text--fontPos13--1DoEt text--_fontBase--YWDo0"><a class="basic_form--inlineLink--3sRG- blue_link--blueLink--22X56 " rel="noopener">Upgrade your team</a> for unlimited design files, projects, and shared team libraries.</div></div><div class="file_browser_page_view--contentContainer--qrxOf "><div class="team_page_view--tabContentContainer--2UILg"><div class="view_bar--container--24m40 "><div class="view_bar--leftSide--2c0jw"><div class="tile_sort_filter--dropdownContainer--2BgAd text--fontPos11--RSei3 text--_fontBase--YWDo0 "><span>Last modified</span><div class="tile_sort_filter--caretContainer--21PSd"><span class="svg-container tile_sort_filter--caret--3BwD_ "><svg class="svg" width="6" height="6" viewBox="0 0 6 6" xmlns="http://www.w3.org/2000/svg"><path d="M1.06 1.475L.708 1.12 0 1.828l.354.354.707-.707zM2.829 3.95l-.353.353.353.354.354-.354-.354-.353zm2.475-1.768l.354-.354-.707-.707-.354.354.707.707zm-4.95 0l2.122 2.121.707-.707-2.121-2.121-.707.707zm2.829 2.121l2.121-2.121-.707-.707-2.121 2.121.707.707z" fill-rule="nonzero" fill-opacity="1" fill="#000" stroke="none"></path></svg></span></div></div></div><div class="view_bar--rightSide--2rOlY"><div class="view_mode_toggle--listViewIcon--tLpbE"><span tabindex="0" class="svg-container option_button--toggled--2-LLL option_button--_optionButton--lWjmC view_mode_toggle--optionButtonToggled--4wf-t view_mode_toggle--_optionButton--21kTT" data-tooltip-type="text" data-tooltip="Show as grid"><svg class="svg" width="12" height="12" viewBox="0 0 12 12" xmlns="http://www.w3.org/2000/svg"><path d="M1 1h3v3H1V1zM0 0h5v5H0V0zm1 8h3v3H1V8zM0 7h5v5H0V7zm11-6H8v3h3V1zM8 0H7v5h5V0H8zm0 8h3v3H8V8zM7 7h5v5H7V7z" fill-rule="evenodd" fill-opacity="1" fill="#000" stroke="none"></path></svg></span><span tabindex="0" class="svg-container option_button--untoggled--2KWMQ option_button--_optionButton--lWjmC view_mode_toggle--optionButtonUntoggled--260VM view_mode_toggle--_optionButton--21kTT" data-tooltip-type="text" data-tooltip="Show as list"><svg class="svg" width="14" height="11" viewBox="0 0 14 11" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h14v1H0V0zm0 5h14v1H0V5zm14 5H0v1h14v-1z" fill-rule="evenodd" fill-opacity=".8" fill="#000" stroke="none"></path></svg></span></div></div></div><div class="folder_list_view--foldersContainerList--14Wwr"><div class="folder_list_card--folderCard--LTX9e" data-onboarding-key="project-card"><div></div><div class="folder_list_card--folderInfoTile--3I-ii folder_list_card--_fileTileContainer--2lbvg"><div class="folder_list_card--folderUpperRow--1EgXe"><div class="folder_list_card--folderName--1uCDF text--fontPos13--1DoEt text--_fontBase--YWDo0">Web Design</div></div><div class="folder_list_card--folderDescription--25k4E ellipsis--ellipsisAfter3Lines--30mso ellipsis--_ellipsisAfterNLines--26JkZ">Files in your team project can be accessed by any team member.</div><div class="folder_list_card--folderInfoFooter--145rW"><div class="folder_subscribe_star--svgContainer--3rC1c" data-tooltip-type="text" data-tooltip="Add to Favorites" data-tooltip-timeout-delay="50" data-tooltip-offset-y="-4"><span class="svg-container folder_subscribe_star--starSubscribed--22az4"><svg class="svg" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg"><path d="M8 .5l2 5h5L11 9l1.5 5L8 11l-4.5 3.068L5 8.885 1 5.5h5l2-5z" fill-rule="nonzero" fill-opacity="1" fill="#000" stroke="none"></path></svg></span></div><div class="folder_list_card--folderActivity--Am89J">2 files, updated <span class="">7 minutes ago</span></div></div></div><div class="folder_list_card--folderTiles--2uTi0"><a class="folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg" href="https://www.figma.com/file/V5z5KTS6cEwGh7knE1Qjva/Team-Discussion" rel="noopener" draggable="false"><div class="folder_list_card--image--2eURH" style="background: url(&quot;data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHJlY3QgZmlsbD0iI0ZGRkZGRiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+PHBhdGggZmlsbD0iI0YxRjFGMSIgZD0iTSAwIDggSCAxNiBWIDAgSCA4IFYgMTYgSCAwIi8+PC9zdmc+&quot;);"><div class="folder_list_card--whiteboardThumbnailContainer--1XCSn generic_tile_thumbnail--whiteboardThumbnail--11QcH generic_tile_thumbnail--thumbnailContainer--2OJUh" style="background-color: rgb(229, 229, 229);"><div class="folder_list_card--thumbnail--3R3v2" style="background-image: url(&quot;https://s3-alpha-sig.figma.com/thumbnails/V5z5KTS6cEwGh7knE1Qjva/default?Expires=1632700800&amp;Signature=A0itiDzZ7Ot7L6BUHvLGR2m9-87iAXPaoqCICqNYblsPyb1-ii3OmOxiDDeVI9s7sb6JNeqtyCgIoOAGH2O03xEMsNtonIwajU50aTmCsni8S93606ZBS3KpjI1CNW-HaszA-Tvcglqkovaua7Ar3RFerXr-6ggs49NTqlp5xD50bALFt2pJSkhz0~Als844Zg-trWKBhnwfCuyyXqVBmyejB4ZEGR3V1fbGdmmIKAZ7Xu6xB7LS7Gcsb~UWpsWoYHYNFkUz-pwVi8c2JSVk7UWlawG8~pzpb~zrmSOKaE3VtoDGIOmiGh5BrSJUhb1v4pk6xGxl-bC-bIq9HmMrQw__&amp;Key-Pair-Id=APKAINTVSUGEWH5XD5UA&quot;);"></div></div></div><div class="folder_list_card--fileName--21voK ellipsis--ellipsis--1RWY6">Team Discussion</div></a><a class="folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg" href="https://www.figma.com/file/vkCd83TgyBA1EbOXFlh6nU/Web-Design" rel="noopener" draggable="false"><div class="folder_list_card--image--2eURH" style="background: url(&quot;data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHJlY3QgZmlsbD0iI0ZGRkZGRiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+PHBhdGggZmlsbD0iI0YxRjFGMSIgZD0iTSAwIDggSCAxNiBWIDAgSCA4IFYgMTYgSCAwIi8+PC9zdmc+&quot;);"><div class="folder_list_card--thumbnailContainer--iOXoU generic_tile_thumbnail--thumbnailContainer--2OJUh" style="background-color: rgb(229, 229, 229);"><div class="folder_list_card--thumbnail--3R3v2" style="background-image: url(&quot;https://s3-alpha-sig.figma.com/thumbnails/vkCd83TgyBA1EbOXFlh6nU/default?Expires=1632700800&amp;Signature=Ab4cRR3TFMN2UwBbmWF~7asCfjxTVHb3MrN3LmyR1EyhezvuAEU2wZIDOopaa3-nT906QpwwSAQILdrGl1m19qJcqbaMGEjcWZhXtw7fH5o0aOB1BVyT44NvS4FWTZzutA2uV6TjDTmrQ~kBDc0L~cDgMe1tkk~VOaIxgwylx1TwChJUdb-8v~Q85KoZ-WXYbWEwbaDNN9vj-wXVCyJgHUlfTyazv4Sd4q2Z~oDFAabWgjMVDjQzkRTAwVIQZcvNJ68wg0ksL7X5ZYNY3UVnoAa-cvyn7pX4MZmyw1EbmqElC~fZwhsI6pHlCAJ37sqZH-6eCRRfPjgwXFXXcYcZIw__&amp;Key-Pair-Id=APKAINTVSUGEWH5XD5UA&quot;);"></div></div></div><div class="folder_list_card--fileName--21voK ellipsis--ellipsis--1RWY6">Web Design</div></a><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div><div class="folder_list_card--invisibleFileTile--3Uo1J folder_list_card--fileTile--FYSue folder_list_card--_fileTileContainer--2lbvg"></div></div></div></div></div></div></div></div></div><div class="flash_view--flashes--1wuM5"></div><div class="visual_bell--base--3awBi"><div class="visual_bell--messageContainer--1XPoQ _overlayBase--_overlayBase--1sCqN text--fontNeg14--uh3vw text--_fontBase--YWDo0 text--_whiteText--2PkdM "></div></div><div class="blocked_ui_loading_indicator--base--3rACw"><div class="blocked_ui_loading_indicator--messageContainer--2KyaR _overlayBase--_overlayBase--1sCqN text--fontNeg14--uh3vw text--_fontBase--YWDo0 text--_whiteText--2PkdM "></div></div><div></div><div></div><div class="help_widget--helpWidget--22IIi text--_whiteText--2PkdM" style="margin-bottom: 0px;"><span class="svg-container help_widget--clickableSvg--2qCOm"><svg class="svg" width="8" height="14" viewBox="0 0 8 14" xmlns="http://www.w3.org/2000/svg"><path d="M5 13H4v1h1v-1zM4 1C2.343 1 1 2.343 1 4H0c0-2.21 1.79-4 4-4 2.21 0 4 1.79 4 4 0 1.268-.59 2.398-1.51 3.13l-.083.065C5.553 7.833 5 8.852 5 10H4c0-1.424.662-2.694 1.694-3.518l.083-.064C6.519 5.87 7 4.992 7 4c0-1.657-1.343-3-3-3z" fill-rule="nonzero" fill-opacity="1" fill="#fff" stroke="none"></path></svg></span><div class="zendesk-web-widget"></div><div class="help_widget--tooltip--jXoVZ help_widget--tooltipPosition--2HJXE" style="margin-bottom: 0px;">Help and resources</div></div><iframe aria-hidden="true" tabindex="-1" name="gtm-iframe" src="https://marketing.figma.com?referrer=https://www.figma.com/?fuid=1019473611201361470&amp;team_name=Web+Squad&amp;team_role_redemption=300&amp;temp-cache-bust=1" style="width: 0px; height: 0px; display: none; visibility: hidden;"></iframe></div></div></div>

    <div id="filebrowser-loading-page" class="fadeOut hidden">
  <div class="navbar"></div>

  <!-- HAX: this sidebar is cloned and used outside of this page -->
  <div id="filebrowser-loading-sidebar" class="filebrowser-loading-sidebar">
    <div class="row">
      <div class="circle"></div>
    </div>
    <div class="row"></div>
    <div class="row"></div>
    <div class="row"></div>
    <div class="divider"></div>
    <div class="row">
      <div class="circle"></div>
    </div>
    <div class="row"></div>
    <div class="divider"></div>
    <div class="row"></div>
    <div class="row"></div>
    <div class="row"></div>
  </div>

  <div class="page">

    <div class="toolbar">
      <div class="item"></div>
    </div>



    <div class="columns">


      <div class="right-column">
        <div class="row"></div>
        <div class="row"></div>
        <div class="row"></div>
        <div class="row"></div>
        <div class="row"></div>
        <div class="row"></div>
        <div class="row"></div>
        <div class="row">
          <div class="circle"></div>
        </div>
        <div class="row">
          <div class="circle"></div>
        </div>
      </div>


      <div class="content">


        <div class="sort-dropdown"></div>
        <div class="project-grid">
          <div class="card">
            <div class="left">
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
            </div>
            <div class="right">
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
            </div>
          </div>
          <div class="card">
            <div class="left">
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
            </div>
            <div class="right">
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
            </div>
          </div>
          <div class="card">
            <div class="left">
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
            </div>
            <div class="right">
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
            </div>
          </div>
          <div class="card">
            <div class="left">
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
            </div>
            <div class="right">
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
              <div class="row"></div>
            </div>
          </div>
        </div>


      </div>

    </div>
  </div>

  <div id="filebrowser-loading-progress-bar"></div>
</div>


    

      <script nonce="">
    window['sentryConfig'] = {
      id: 1019473611201361470,
    }
  </script>

      <script nonce="" src="https://www.figma.com/figbuild-artifacts/figma_app.8907f32e607f8406f0a1a1265d55a85c.min.js.br"></script>

  

</body></html>
"""
    return HttpResponse(html)