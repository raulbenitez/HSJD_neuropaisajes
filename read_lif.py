




<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-veKG2ootplNGLwNEW5It4+lJXwpdOVR1Ry4MBDNvdgL6OgBkiAXaZAZnIKkw6sIygnfGqQhR5q7UdS1llqd6/g==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-bde286da8a2da653462f03445b922de3.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-oskjA1HEwZq5HoCKRZWoUhAoBLeFfX5lCdbSsUB2Bkemb1XNH7rXMMrxJ+YTQMunfXVXY1eRDeEyL0527syBBw==" rel="stylesheet" href="https://github.githubassets.com/assets/github-a2c9230351c4c19ab91e808a4595a852.css" />
    
    
    
    


  <meta name="viewport" content="width=device-width">
  
  <title>MITO_FIBERS/read_lif.py at master · raulbenitez/MITO_FIBERS</title>
    <meta name="description" content="Contribute to raulbenitez/MITO_FIBERS development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars0.githubusercontent.com/u/34841791?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="raulbenitez/MITO_FIBERS" /><meta name="twitter:description" content="Contribute to raulbenitez/MITO_FIBERS development by creating an account on GitHub." />
    <meta property="og:image" content="https://avatars0.githubusercontent.com/u/34841791?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="raulbenitez/MITO_FIBERS" /><meta property="og:url" content="https://github.com/raulbenitez/MITO_FIBERS" /><meta property="og:description" content="Contribute to raulbenitez/MITO_FIBERS development by creating an account on GitHub." />

  <link rel="assets" href="https://github.githubassets.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6NTAzMzM1MjYyOjEyNTQ4NmU4YWMwNDFlOWVmZjZiYjk3YzZhNmIxZDRkYjA3NDIxY2EzN2VhN2ZkNTQ0NjRkMWYzYjhiNmRmNGM=--bc7db4cd28b18c514f07e3c1b20b4132b583406f">
  <link rel="sudo-modal" href="/sessions/sudo_modal">

  <meta name="request-id" content="D79E:E6F9:BDC42E:10FCD83:5EDA21B3" data-pjax-transient="true" /><meta name="html-safe-nonce" content="305099cf7f68fcef66eb26e1be2b41b27f1cdd8d" data-pjax-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9yYXVsYmVuaXRlei9NSVRPX0ZJQkVSUyIsInJlcXVlc3RfaWQiOiJENzlFOkU2Rjk6QkRDNDJFOjEwRkNEODM6NUVEQTIxQjMiLCJ2aXNpdG9yX2lkIjoiNjcyMTc1MTA4ODI5MTMxNDIxMSIsInJlZ2lvbl9lZGdlIjoiYW1zIiwicmVnaW9uX3JlbmRlciI6ImlhZCJ9" data-pjax-transient="true" /><meta name="visitor-hmac" content="484f6bcf18061e106d7f4e3293984c073e6402ba4c61824f37bb3921248f53d7" data-pjax-transient="true" />



  <meta name="github-keyboard-shortcuts" content="repository,source-code" data-pjax-transient="true" />

  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-ga_id" content="" class="js-octo-ga-id" /><meta name="octolytics-actor-id" content="34841791" /><meta name="octolytics-actor-login" content="raulbenitez" /><meta name="octolytics-actor-hash" content="25b21d70d1b8e5b8c3cd65194f8edd5cf9b8af7b8536fd0346b9320b69e940bb" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />


<meta name="optimizely-sdk-key" content="cowimJNste4j7QnBNCjaw" />

    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="2ccbbac406d6dfc89e9cd07cf2e2cdfe">

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="raulbenitez">


      <meta name="expected-hostname" content="github.com">

      <meta name="js-proxy-site-detection-payload" content="ODE2NTFlZmZlZjQ4ZDA4MDc2YWI4MDRkZjQwMjVhNWY4NTc4NGVkYmVhODIzM2RjMDMwYzIyZDQ2YzQyMmVlY3x7InJlbW90ZV9hZGRyZXNzIjoiMTkzLjE1Mi4xNDUuMjIyIiwicmVxdWVzdF9pZCI6IkQ3OUU6RTZGOTpCREM0MkU6MTBGQ0Q4Mzo1RURBMjFCMyIsInRpbWVzdGFtcCI6MTU5MTM1Mzc4OCwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="MARKETPLACE_PENDING_INSTALLATIONS,PAGE_STALE_CHECK,JS_CHUNKING">

  <meta http-equiv="x-pjax-version" content="5dc3948fdb08ba2fed5808d60d00784e">
  

      <link href="https://github.com/raulbenitez/MITO_FIBERS/commits/master.atom" rel="alternate" title="Recent Commits to MITO_FIBERS:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/raulbenitez/MITO_FIBERS git https://github.com/raulbenitez/MITO_FIBERS.git">

  <meta name="octolytics-dimension-user_id" content="34841791" /><meta name="octolytics-dimension-user_login" content="raulbenitez" /><meta name="octolytics-dimension-repository_id" content="265504996" /><meta name="octolytics-dimension-repository_nwo" content="raulbenitez/MITO_FIBERS" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="265504996" /><meta name="octolytics-dimension-repository_network_root_nwo" content="raulbenitez/MITO_FIBERS" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="true" />


    <link rel="canonical" href="https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive page-blob">
    

    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
      <span class="Progress progress-pjax-loader position-fixed width-full js-pjax-loader-bar">
        <span class="progress-pjax-loader-bar top-0 left-0" style="width: 0%;"></span>
      </span>

      
      



          <header class="Header py-lg-0 js-details-container Details flex-wrap flex-lg-nowrap p-responsive" role="banner">
  <div class="Header-item d-none d-lg-flex">
    <a class="Header-link" href="https://github.com/" data-hotkey="g d"
  aria-label="Homepage " data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8C0 11.54 2.29 14.53 5.47 15.59C5.87 15.66 6.02 15.42 6.02 15.21C6.02 15.02 6.01 14.39 6.01 13.72C4 14.09 3.48 13.23 3.32 12.78C3.23 12.55 2.84 11.84 2.5 11.65C2.22 11.5 1.82 11.13 2.49 11.12C3.12 11.11 3.57 11.7 3.72 11.94C4.44 13.15 5.59 12.81 6.05 12.6C6.12 12.08 6.33 11.73 6.56 11.53C4.78 11.33 2.92 10.64 2.92 7.58C2.92 6.71 3.23 5.99 3.74 5.43C3.66 5.23 3.38 4.41 3.82 3.31C3.82 3.31 4.49 3.1 6.02 4.13C6.66 3.95 7.34 3.86 8.02 3.86C8.7 3.86 9.38 3.95 10.02 4.13C11.55 3.09 12.22 3.31 12.22 3.31C12.66 4.41 12.38 5.23 12.3 5.43C12.81 5.99 13.12 6.7 13.12 7.58C13.12 10.65 11.25 11.33 9.47 11.53C9.76 11.78 10.01 12.26 10.01 13.01C10.01 14.08 10 14.94 10 15.21C10 15.42 10.15 15.67 10.55 15.59C13.71 14.53 16 11.53 16 8C16 3.58 12.42 0 8 0Z"></path></svg>
</a>

  </div>

  <div class="Header-item d-lg-none">
    <button class="Header-link btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
      <svg height="24" class="octicon octicon-three-bars" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1 2.75C1 2.55109 1.07902 2.36032 1.21967 2.21967C1.36032 2.07902 1.55109 2 1.75 2H14.25C14.4489 2 14.6397 2.07902 14.7803 2.21967C14.921 2.36032 15 2.55109 15 2.75C15 2.94891 14.921 3.13968 14.7803 3.28033C14.6397 3.42098 14.4489 3.5 14.25 3.5H1.75C1.55109 3.5 1.36032 3.42098 1.21967 3.28033C1.07902 3.13968 1 2.94891 1 2.75ZM1 7.75C1 7.55109 1.07902 7.36032 1.21967 7.21967C1.36032 7.07902 1.55109 7 1.75 7H14.25C14.4489 7 14.6397 7.07902 14.7803 7.21967C14.921 7.36032 15 7.55109 15 7.75C15 7.94891 14.921 8.13968 14.7803 8.28033C14.6397 8.42098 14.4489 8.5 14.25 8.5H1.75C1.55109 8.5 1.36032 8.42098 1.21967 8.28033C1.07902 8.13968 1 7.94891 1 7.75ZM1.75 12C1.55109 12 1.36032 12.079 1.21967 12.2197C1.07902 12.3603 1 12.5511 1 12.75C1 12.9489 1.07902 13.1397 1.21967 13.2803C1.36032 13.421 1.55109 13.5 1.75 13.5H14.25C14.4489 13.5 14.6397 13.421 14.7803 13.2803C14.921 13.1397 15 12.9489 15 12.75C15 12.5511 14.921 12.3603 14.7803 12.2197C14.6397 12.079 14.4489 12 14.25 12H1.75Z"></path></svg>
    </button>
  </div>

  <div class="Header-item Header-item--full flex-column flex-lg-row width-full flex-order-2 flex-lg-order-none mr-0 mr-lg-3 mt-3 mt-lg-0 Details-content--hidden">
      <div class="header-search flex-self-stretch flex-lg-self-auto mr-0 mr-lg-3 mb-3 mb-lg-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="265504996" data-scoped-search-url="/raulbenitez/MITO_FIBERS/search" data-unscoped-search-url="/search" action="/raulbenitez/MITO_FIBERS/search" accept-charset="UTF-8" method="get">
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations"
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" value="QvkV80dVzDLCPQYAQHmQMoeMd5YBTM9N4po80q0PHz2ppcfKsUPhdafS2H7md/4rR/EKO0z16mxiDSGrZm5Mrw==" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M2 2.5C2 1.83696 2.26339 1.20107 2.73223 0.732233C3.20108 0.263392 3.83696 0 4.5 0L13.25 0C13.4489 0 13.6397 0.0790176 13.7803 0.21967C13.921 0.360322 14 0.551088 14 0.75V13.25C14 13.4489 13.921 13.6397 13.7803 13.7803C13.6397 13.921 13.4489 14 13.25 14H10.75C10.5511 14 10.3603 13.921 10.2197 13.7803C10.079 13.6397 10 13.4489 10 13.25C10 13.0511 10.079 12.8603 10.2197 12.7197C10.3603 12.579 10.5511 12.5 10.75 12.5H12.5V10.5H4.5C4.30308 10.5 4.11056 10.5582 3.94657 10.6672C3.78257 10.7762 3.65442 10.9312 3.57816 11.1128C3.50191 11.2943 3.48096 11.4943 3.51793 11.6878C3.5549 11.8812 3.64816 12.0594 3.786 12.2C3.92524 12.3422 4.0023 12.5338 4.00024 12.7328C3.99818 12.9318 3.91716 13.1218 3.775 13.261C3.63285 13.4002 3.4412 13.4773 3.24222 13.4752C3.04325 13.4732 2.85324 13.3922 2.714 13.25C2.25571 12.7829 1.99929 12.1544 2 11.5V2.5ZM12.5 1.5V9H4.5C4.144 9 3.806 9.074 3.5 9.208V2.5C3.5 2.23478 3.60536 1.98043 3.79289 1.79289C3.98043 1.60536 4.23478 1.5 4.5 1.5H12.5ZM5 12.25V15.5C5 15.5464 5.01293 15.5919 5.03734 15.6314C5.06175 15.6709 5.09667 15.7028 5.1382 15.7236C5.17972 15.7444 5.22621 15.7532 5.27245 15.749C5.31869 15.7448 5.36286 15.7279 5.4 15.7L6.85 14.613C6.89328 14.5805 6.94591 14.563 7 14.563C7.05409 14.563 7.10673 14.5805 7.15 14.613L8.6 15.7C8.63714 15.7279 8.68131 15.7448 8.72755 15.749C8.77379 15.7532 8.82028 15.7444 8.8618 15.7236C8.90333 15.7028 8.93826 15.6709 8.96266 15.6314C8.98707 15.5919 9 15.5464 9 15.5V12.25C9 12.1837 8.97366 12.1201 8.92678 12.0732C8.87989 12.0263 8.81631 12 8.75 12H5.25C5.1837 12 5.12011 12.0263 5.07322 12.0732C5.02634 12.1201 5 12.1837 5 12.25Z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.75 0C0.783502 0 0 0.783501 0 1.75V14.25C0 15.2165 0.783501 16 1.75 16H14.25C15.2165 16 16 15.2165 16 14.25V1.75C16 0.783502 15.2165 0 14.25 0H1.75ZM1.5 1.75C1.5 1.61193 1.61193 1.5 1.75 1.5H14.25C14.3881 1.5 14.5 1.61193 14.5 1.75V14.25C14.5 14.3881 14.3881 14.5 14.25 14.5H1.75C1.61193 14.5 1.5 14.3881 1.5 14.25V1.75ZM11.75 3C11.3358 3 11 3.33579 11 3.75V11.25C11 11.6642 11.3358 12 11.75 12C12.1642 12 12.5 11.6642 12.5 11.25V3.75C12.5 3.33579 12.1642 3 11.75 3ZM3.5 3.75C3.5 3.33579 3.83579 3 4.25 3C4.66421 3 5 3.33579 5 3.75V9.25C5 9.66421 4.66421 10 4.25 10C3.83579 10 3.5 9.66421 3.5 9.25V3.75ZM8 3C7.58579 3 7.25 3.33579 7.25 3.75V7.25C7.25 7.66421 7.58579 8 8 8C8.41421 8 8.75 7.66421 8.75 7.25V3.75C8.75 3.33579 8.41421 3 8 3Z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.5 7C11.5 7.59094 11.3836 8.17611 11.1574 8.72207C10.9313 9.26804 10.5998 9.76411 10.182 10.182C9.7641 10.5998 9.26803 10.9313 8.72206 11.1575C8.1761 11.3836 7.59094 11.5 6.99999 11.5C6.40904 11.5 5.82388 11.3836 5.27791 11.1575C4.73195 10.9313 4.23587 10.5998 3.81801 10.182C3.40014 9.76411 3.06868 9.26804 2.84253 8.72207C2.61638 8.17611 2.49999 7.59094 2.49999 7C2.49999 5.80652 2.97409 4.66193 3.81801 3.81802C4.66192 2.9741 5.80651 2.5 6.99999 2.5C8.19346 2.5 9.33805 2.9741 10.182 3.81802C11.0259 4.66193 11.5 5.80652 11.5 7ZM10.68 11.74C9.47437 12.676 7.95736 13.1173 6.43779 12.9741C4.91822 12.831 3.51033 12.1141 2.50074 10.9694C1.49114 9.82471 0.95574 8.33829 1.00352 6.81275C1.05131 5.2872 1.67869 3.8372 2.75794 2.75795C3.8372 1.6787 5.28719 1.05132 6.81274 1.00353C8.33829 0.955747 9.8247 1.49115 10.9694 2.50075C12.1141 3.51034 12.831 4.91823 12.9741 6.4378C13.1173 7.95736 12.676 9.47437 11.74 10.68L14.78 13.72C14.8537 13.7887 14.9128 13.8715 14.9538 13.9635C14.9948 14.0555 15.0168 14.1548 15.0186 14.2555C15.0204 14.3562 15.0018 14.4562 14.9641 14.5496C14.9264 14.643 14.8702 14.7278 14.799 14.799C14.7278 14.8703 14.643 14.9264 14.5496 14.9641C14.4562 15.0018 14.3562 15.0204 14.2555 15.0186C14.1548 15.0168 14.0554 14.9948 13.9635 14.9538C13.8715 14.9128 13.7887 14.8537 13.72 14.78L10.68 11.74Z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M2 2.5C2 1.83696 2.26339 1.20107 2.73223 0.732233C3.20108 0.263392 3.83696 0 4.5 0L13.25 0C13.4489 0 13.6397 0.0790176 13.7803 0.21967C13.921 0.360322 14 0.551088 14 0.75V13.25C14 13.4489 13.921 13.6397 13.7803 13.7803C13.6397 13.921 13.4489 14 13.25 14H10.75C10.5511 14 10.3603 13.921 10.2197 13.7803C10.079 13.6397 10 13.4489 10 13.25C10 13.0511 10.079 12.8603 10.2197 12.7197C10.3603 12.579 10.5511 12.5 10.75 12.5H12.5V10.5H4.5C4.30308 10.5 4.11056 10.5582 3.94657 10.6672C3.78257 10.7762 3.65442 10.9312 3.57816 11.1128C3.50191 11.2943 3.48096 11.4943 3.51793 11.6878C3.5549 11.8812 3.64816 12.0594 3.786 12.2C3.92524 12.3422 4.0023 12.5338 4.00024 12.7328C3.99818 12.9318 3.91716 13.1218 3.775 13.261C3.63285 13.4002 3.4412 13.4773 3.24222 13.4752C3.04325 13.4732 2.85324 13.3922 2.714 13.25C2.25571 12.7829 1.99929 12.1544 2 11.5V2.5ZM12.5 1.5V9H4.5C4.144 9 3.806 9.074 3.5 9.208V2.5C3.5 2.23478 3.60536 1.98043 3.79289 1.79289C3.98043 1.60536 4.23478 1.5 4.5 1.5H12.5ZM5 12.25V15.5C5 15.5464 5.01293 15.5919 5.03734 15.6314C5.06175 15.6709 5.09667 15.7028 5.1382 15.7236C5.17972 15.7444 5.22621 15.7532 5.27245 15.749C5.31869 15.7448 5.36286 15.7279 5.4 15.7L6.85 14.613C6.89328 14.5805 6.94591 14.563 7 14.563C7.05409 14.563 7.10673 14.5805 7.15 14.613L8.6 15.7C8.63714 15.7279 8.68131 15.7448 8.72755 15.749C8.77379 15.7532 8.82028 15.7444 8.8618 15.7236C8.90333 15.7028 8.93826 15.6709 8.96266 15.6314C8.98707 15.5919 9 15.5464 9 15.5V12.25C9 12.1837 8.97366 12.1201 8.92678 12.0732C8.87989 12.0263 8.81631 12 8.75 12H5.25C5.1837 12 5.12011 12.0263 5.07322 12.0732C5.02634 12.1201 5 12.1837 5 12.25Z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.75 0C0.783502 0 0 0.783501 0 1.75V14.25C0 15.2165 0.783501 16 1.75 16H14.25C15.2165 16 16 15.2165 16 14.25V1.75C16 0.783502 15.2165 0 14.25 0H1.75ZM1.5 1.75C1.5 1.61193 1.61193 1.5 1.75 1.5H14.25C14.3881 1.5 14.5 1.61193 14.5 1.75V14.25C14.5 14.3881 14.3881 14.5 14.25 14.5H1.75C1.61193 14.5 1.5 14.3881 1.5 14.25V1.75ZM11.75 3C11.3358 3 11 3.33579 11 3.75V11.25C11 11.6642 11.3358 12 11.75 12C12.1642 12 12.5 11.6642 12.5 11.25V3.75C12.5 3.33579 12.1642 3 11.75 3ZM3.5 3.75C3.5 3.33579 3.83579 3 4.25 3C4.66421 3 5 3.33579 5 3.75V9.25C5 9.66421 4.66421 10 4.25 10C3.83579 10 3.5 9.66421 3.5 9.25V3.75ZM8 3C7.58579 3 7.25 3.33579 7.25 3.75V7.25C7.25 7.66421 7.58579 8 8 8C8.41421 8 8.75 7.66421 8.75 7.25V3.75C8.75 3.33579 8.41421 3 8 3Z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.5 7C11.5 7.59094 11.3836 8.17611 11.1574 8.72207C10.9313 9.26804 10.5998 9.76411 10.182 10.182C9.7641 10.5998 9.26803 10.9313 8.72206 11.1575C8.1761 11.3836 7.59094 11.5 6.99999 11.5C6.40904 11.5 5.82388 11.3836 5.27791 11.1575C4.73195 10.9313 4.23587 10.5998 3.81801 10.182C3.40014 9.76411 3.06868 9.26804 2.84253 8.72207C2.61638 8.17611 2.49999 7.59094 2.49999 7C2.49999 5.80652 2.97409 4.66193 3.81801 3.81802C4.66192 2.9741 5.80651 2.5 6.99999 2.5C8.19346 2.5 9.33805 2.9741 10.182 3.81802C11.0259 4.66193 11.5 5.80652 11.5 7ZM10.68 11.74C9.47437 12.676 7.95736 13.1173 6.43779 12.9741C4.91822 12.831 3.51033 12.1141 2.50074 10.9694C1.49114 9.82471 0.95574 8.33829 1.00352 6.81275C1.05131 5.2872 1.67869 3.8372 2.75794 2.75795C3.8372 1.6787 5.28719 1.05132 6.81274 1.00353C8.33829 0.955747 9.8247 1.49115 10.9694 2.50075C12.1141 3.51034 12.831 4.91823 12.9741 6.4378C13.1173 7.95736 12.676 9.47437 11.74 10.68L14.78 13.72C14.8537 13.7887 14.9128 13.8715 14.9538 13.9635C14.9948 14.0555 15.0168 14.1548 15.0186 14.2555C15.0204 14.3562 15.0018 14.4562 14.9641 14.5496C14.9264 14.643 14.8702 14.7278 14.799 14.799C14.7278 14.8703 14.643 14.9264 14.5496 14.9641C14.4562 15.0018 14.3562 15.0204 14.2555 15.0186C14.1548 15.0168 14.0554 14.9948 13.9635 14.9538C13.8715 14.9128 13.7887 14.8537 13.72 14.78L10.68 11.74Z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M2 2.5C2 1.83696 2.26339 1.20107 2.73223 0.732233C3.20108 0.263392 3.83696 0 4.5 0L13.25 0C13.4489 0 13.6397 0.0790176 13.7803 0.21967C13.921 0.360322 14 0.551088 14 0.75V13.25C14 13.4489 13.921 13.6397 13.7803 13.7803C13.6397 13.921 13.4489 14 13.25 14H10.75C10.5511 14 10.3603 13.921 10.2197 13.7803C10.079 13.6397 10 13.4489 10 13.25C10 13.0511 10.079 12.8603 10.2197 12.7197C10.3603 12.579 10.5511 12.5 10.75 12.5H12.5V10.5H4.5C4.30308 10.5 4.11056 10.5582 3.94657 10.6672C3.78257 10.7762 3.65442 10.9312 3.57816 11.1128C3.50191 11.2943 3.48096 11.4943 3.51793 11.6878C3.5549 11.8812 3.64816 12.0594 3.786 12.2C3.92524 12.3422 4.0023 12.5338 4.00024 12.7328C3.99818 12.9318 3.91716 13.1218 3.775 13.261C3.63285 13.4002 3.4412 13.4773 3.24222 13.4752C3.04325 13.4732 2.85324 13.3922 2.714 13.25C2.25571 12.7829 1.99929 12.1544 2 11.5V2.5ZM12.5 1.5V9H4.5C4.144 9 3.806 9.074 3.5 9.208V2.5C3.5 2.23478 3.60536 1.98043 3.79289 1.79289C3.98043 1.60536 4.23478 1.5 4.5 1.5H12.5ZM5 12.25V15.5C5 15.5464 5.01293 15.5919 5.03734 15.6314C5.06175 15.6709 5.09667 15.7028 5.1382 15.7236C5.17972 15.7444 5.22621 15.7532 5.27245 15.749C5.31869 15.7448 5.36286 15.7279 5.4 15.7L6.85 14.613C6.89328 14.5805 6.94591 14.563 7 14.563C7.05409 14.563 7.10673 14.5805 7.15 14.613L8.6 15.7C8.63714 15.7279 8.68131 15.7448 8.72755 15.749C8.77379 15.7532 8.82028 15.7444 8.8618 15.7236C8.90333 15.7028 8.93826 15.6709 8.96266 15.6314C8.98707 15.5919 9 15.5464 9 15.5V12.25C9 12.1837 8.97366 12.1201 8.92678 12.0732C8.87989 12.0263 8.81631 12 8.75 12H5.25C5.1837 12 5.12011 12.0263 5.07322 12.0732C5.02634 12.1201 5 12.1837 5 12.25Z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.75 0C0.783502 0 0 0.783501 0 1.75V14.25C0 15.2165 0.783501 16 1.75 16H14.25C15.2165 16 16 15.2165 16 14.25V1.75C16 0.783502 15.2165 0 14.25 0H1.75ZM1.5 1.75C1.5 1.61193 1.61193 1.5 1.75 1.5H14.25C14.3881 1.5 14.5 1.61193 14.5 1.75V14.25C14.5 14.3881 14.3881 14.5 14.25 14.5H1.75C1.61193 14.5 1.5 14.3881 1.5 14.25V1.75ZM11.75 3C11.3358 3 11 3.33579 11 3.75V11.25C11 11.6642 11.3358 12 11.75 12C12.1642 12 12.5 11.6642 12.5 11.25V3.75C12.5 3.33579 12.1642 3 11.75 3ZM3.5 3.75C3.5 3.33579 3.83579 3 4.25 3C4.66421 3 5 3.33579 5 3.75V9.25C5 9.66421 4.66421 10 4.25 10C3.83579 10 3.5 9.66421 3.5 9.25V3.75ZM8 3C7.58579 3 7.25 3.33579 7.25 3.75V7.25C7.25 7.66421 7.58579 8 8 8C8.41421 8 8.75 7.66421 8.75 7.25V3.75C8.75 3.33579 8.41421 3 8 3Z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.5 7C11.5 7.59094 11.3836 8.17611 11.1574 8.72207C10.9313 9.26804 10.5998 9.76411 10.182 10.182C9.7641 10.5998 9.26803 10.9313 8.72206 11.1575C8.1761 11.3836 7.59094 11.5 6.99999 11.5C6.40904 11.5 5.82388 11.3836 5.27791 11.1575C4.73195 10.9313 4.23587 10.5998 3.81801 10.182C3.40014 9.76411 3.06868 9.26804 2.84253 8.72207C2.61638 8.17611 2.49999 7.59094 2.49999 7C2.49999 5.80652 2.97409 4.66193 3.81801 3.81802C4.66192 2.9741 5.80651 2.5 6.99999 2.5C8.19346 2.5 9.33805 2.9741 10.182 3.81802C11.0259 4.66193 11.5 5.80652 11.5 7ZM10.68 11.74C9.47437 12.676 7.95736 13.1173 6.43779 12.9741C4.91822 12.831 3.51033 12.1141 2.50074 10.9694C1.49114 9.82471 0.95574 8.33829 1.00352 6.81275C1.05131 5.2872 1.67869 3.8372 2.75794 2.75795C3.8372 1.6787 5.28719 1.05132 6.81274 1.00353C8.33829 0.955747 9.8247 1.49115 10.9694 2.50075C12.1141 3.51034 12.831 4.91823 12.9741 6.4378C13.1173 7.95736 12.676 9.47437 11.74 10.68L14.78 13.72C14.8537 13.7887 14.9128 13.8715 14.9538 13.9635C14.9948 14.0555 15.0168 14.1548 15.0186 14.2555C15.0204 14.3562 15.0018 14.4562 14.9641 14.5496C14.9264 14.643 14.8702 14.7278 14.799 14.799C14.7278 14.8703 14.643 14.9264 14.5496 14.9641C14.4562 15.0018 14.3562 15.0204 14.2555 15.0186C14.1548 15.0168 14.0554 14.9948 13.9635 14.9538C13.8715 14.9128 13.7887 14.8537 13.72 14.78L10.68 11.74Z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>


    <nav class="d-flex flex-column flex-lg-row flex-self-stretch flex-lg-self-auto" aria-label="Global">
    <a class="Header-link py-lg-3 d-block d-lg-none py-2 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">
      Dashboard
</a>
  <a class="js-selected-navigation-item Header-link py-lg-3  mr-0 mr-lg-3 py-2 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
    Pull requests
</a>
  <a class="js-selected-navigation-item Header-link py-lg-3  mr-0 mr-lg-3 py-2 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
    Issues
</a>

    <div class="mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15">
      <a class="js-selected-navigation-item Header-link py-lg-3 d-inline-block" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
        Marketplace
</a>      

    </div>

  <a class="js-selected-navigation-item Header-link py-lg-3  mr-0 mr-lg-3 py-2 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
    Explore
</a>


    <a class="Header-link d-block d-lg-none mr-0 mr-lg-3 py-2 py-lg-3 border-top border-lg-top-0 border-white-fade-15" href="/raulbenitez">
      <img class="avatar avatar-user" src="https://avatars3.githubusercontent.com/u/34841791?s=40&amp;v=4" width="20" height="20" alt="@raulbenitez" />
      raulbenitez
</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="oEQ49HRXB5GCzr/3M/dSabjsIRSYGTgx4zJLqbUQC2XvLg6w5/AA+gfiHmWkE6Vgg8QLqqZo4Nnz83I4tzv68Q==" />
      <button type="submit" class="Header-link mr-0 mr-lg-3 py-2 py-lg-3 border-top border-lg-top-0 border-white-fade-15 d-lg-none btn-link d-block width-full text-left" data-ga-click="Header, sign out, icon:logout" style="padding-left: 2px;">
        <svg class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M2 2.75C2 1.7835 2.7835 1 3.75 1H6.25C6.66421 1 7 1.33579 7 1.75C7 2.16421 6.66421 2.5 6.25 2.5H3.75C3.61193 2.5 3.5 2.61193 3.5 2.75V13.25C3.5 13.3881 3.61193 13.5 3.75 13.5H6.25C6.66421 13.5 7 13.8358 7 14.25C7 14.6642 6.66421 15 6.25 15H3.75C2.7835 15 2 14.2165 2 13.25V2.75ZM12.4393 7.25L6.75002 7.25C6.33581 7.25 6.00002 7.58579 6.00002 8C6.00002 8.41422 6.33581 8.75 6.75002 8.75L12.4393 8.75L10.4697 10.7197C10.1768 11.0126 10.1768 11.4874 10.4697 11.7803C10.7626 12.0732 11.2374 12.0732 11.5303 11.7803L14.7803 8.53033C15.0732 8.23744 15.0732 7.76256 14.7803 7.46967L11.5303 4.21967C11.2374 3.92678 10.7626 3.92678 10.4697 4.21967C10.1768 4.51256 10.1768 4.98744 10.4697 5.28033L12.4393 7.25Z"></path></svg>
        Sign out
      </button>
</form></nav>

  </div>

  <div class="Header-item Header-item--full flex-justify-center d-lg-none position-relative">
    <div class="css-truncate css-truncate-target width-fit position-absolute left-0 right-0 text-center">
                <svg class="octicon octicon-repo" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M2 2.5C2 1.83696 2.26339 1.20107 2.73223 0.732233C3.20108 0.263392 3.83696 0 4.5 0L13.25 0C13.4489 0 13.6397 0.0790176 13.7803 0.21967C13.921 0.360322 14 0.551088 14 0.75V13.25C14 13.4489 13.921 13.6397 13.7803 13.7803C13.6397 13.921 13.4489 14 13.25 14H10.75C10.5511 14 10.3603 13.921 10.2197 13.7803C10.079 13.6397 10 13.4489 10 13.25C10 13.0511 10.079 12.8603 10.2197 12.7197C10.3603 12.579 10.5511 12.5 10.75 12.5H12.5V10.5H4.5C4.30308 10.5 4.11056 10.5582 3.94657 10.6672C3.78257 10.7762 3.65442 10.9312 3.57816 11.1128C3.50191 11.2943 3.48096 11.4943 3.51793 11.6878C3.5549 11.8812 3.64816 12.0594 3.786 12.2C3.92524 12.3422 4.0023 12.5338 4.00024 12.7328C3.99818 12.9318 3.91716 13.1218 3.775 13.261C3.63285 13.4002 3.4412 13.4773 3.24222 13.4752C3.04325 13.4732 2.85324 13.3922 2.714 13.25C2.25571 12.7829 1.99929 12.1544 2 11.5V2.5ZM12.5 1.5V9H4.5C4.144 9 3.806 9.074 3.5 9.208V2.5C3.5 2.23478 3.60536 1.98043 3.79289 1.79289C3.98043 1.60536 4.23478 1.5 4.5 1.5H12.5ZM5 12.25V15.5C5 15.5464 5.01293 15.5919 5.03734 15.6314C5.06175 15.6709 5.09667 15.7028 5.1382 15.7236C5.17972 15.7444 5.22621 15.7532 5.27245 15.749C5.31869 15.7448 5.36286 15.7279 5.4 15.7L6.85 14.613C6.89328 14.5805 6.94591 14.563 7 14.563C7.05409 14.563 7.10673 14.5805 7.15 14.613L8.6 15.7C8.63714 15.7279 8.68131 15.7448 8.72755 15.749C8.77379 15.7532 8.82028 15.7444 8.8618 15.7236C8.90333 15.7028 8.93826 15.6709 8.96266 15.6314C8.98707 15.5919 9 15.5464 9 15.5V12.25C9 12.1837 8.97366 12.1201 8.92678 12.0732C8.87989 12.0263 8.81631 12 8.75 12H5.25C5.1837 12 5.12011 12.0263 5.07322 12.0732C5.02634 12.1201 5 12.1837 5 12.25Z"></path></svg>
    <a class="Header-link" href="/raulbenitez">raulbenitez</a>
    /
    <a class="Header-link" href="/raulbenitez/MITO_FIBERS">MITO_FIBERS</a>

</div>
  </div>

  <div class="Header-item mr-0 mr-lg-3 flex-order-1 flex-lg-order-none">
    
    <a aria-label="You have no unread notifications" class="Header-link notification-indicator position-relative tooltipped tooltipped-sw js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:34841791" href="/notifications">
        <span class="js-indicator-modifier mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 16C9.02008 16 9.86178 15.2363 9.98459 14.2495C10.0016 14.1125 9.88807 14 9.75 14H6.25C6.11193 14 5.99836 14.1125 6.01541 14.2495C6.13822 15.2363 6.97992 16 8 16Z"></path>
  <path fill-rule="evenodd" clip-rule="evenodd" d="M8 1.5C6.067 1.5 4.5 3.067 4.5 5V7.94722C4.5 8.29272 4.39773 8.63048 4.20609 8.91795L2.50295 11.4726C2.50103 11.4755 2.5 11.4789 2.5 11.4824C2.5 11.4862 2.50063 11.488 2.50107 11.489C2.50174 11.4906 2.50302 11.4927 2.50515 11.4948C2.50729 11.497 2.50941 11.4983 2.51097 11.4989C2.51204 11.4994 2.51378 11.5 2.51759 11.5H13.4824C13.4862 11.5 13.488 11.4994 13.489 11.4989C13.4906 11.4983 13.4927 11.497 13.4948 11.4948C13.497 11.4927 13.4983 11.4906 13.4989 11.489C13.4994 11.488 13.5 11.4862 13.5 11.4824C13.5 11.4789 13.499 11.4755 13.497 11.4726L11.7939 8.91795C11.6023 8.63048 11.5 8.29272 11.5 7.94722V5C11.5 3.067 9.933 1.5 8 1.5ZM3 5C3 2.23858 5.23858 0 8 0C10.7614 0 13 2.23858 13 5V7.94722C13 7.99658 13.0146 8.04483 13.042 8.0859L14.7451 10.6406C14.9113 10.8899 15 11.1828 15 11.4824C15 12.3206 14.3206 13 13.4824 13H2.51759C1.67945 13 1 12.3206 1 11.4824C1 11.1828 1.08868 10.8899 1.25488 10.6406L2.95801 8.0859C2.98539 8.04483 3 7.99658 3 7.94722V5Z"></path></svg>
</a>
  </div>


  <div class="Header-item position-relative d-none d-lg-flex">
    <details class="details-overlay details-reset">
  <summary class="Header-link"
      aria-label="Create new…"
      data-ga-click="Header, create new, icon:add">
    <svg class="octicon octicon-plus" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8 2C8.41421 2 8.75 2.33579 8.75 2.75V7.25H13.25C13.6642 7.25 14 7.58579 14 8C14 8.41421 13.6642 8.75 13.25 8.75H8.75V13.25C8.75 13.6642 8.41421 14 8 14C7.58579 14 7.25 13.6642 7.25 13.25V8.75H2.75C2.33579 8.75 2 8.41421 2 8C2 7.58579 2.33579 7.25 2.75 7.25H7.25V2.75C7.25 2.33579 7.58579 2 8 2Z"></path></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-n2">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div role="none" class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="raulbenitez/MITO_FIBERS">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/raulbenitez/MITO_FIBERS/issues/new/choose" data-ga-click="Header, create new issue" data-skip-pjax>
      New issue
    </a>


  </details-menu>
</details>

  </div>

  <div class="Header-item position-relative mr-0 d-none d-lg-flex">
    
  <details class="details-overlay details-reset js-feature-preview-indicator-container" data-feature-preview-indicator-src="/users/raulbenitez/feature_preview/indicator_check">

  <summary class="Header-link"
    aria-label="View profile and more"
    data-ga-click="Header, show menu, icon:avatar">
    <img
  alt="@raulbenitez"
  width="20"
  height="20"
  src="https://avatars0.githubusercontent.com/u/34841791?s=60&amp;v=4"
  class="avatar avatar-user " />

      <span class="feature-preview-indicator js-feature-preview-indicator" style="top: 10px;" hidden></span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-n2" style="width: 180px">
    <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/raulbenitez" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">raulbenitez</strong></a></div>
    <div role="none" class="dropdown-divider"></div>

      <div class="pl-3 pr-3 f6 user-status-container js-user-status-context pb-1" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
        
<div class="js-user-status-container
    user-status-compact rounded-1 px-2 py-1 mt-2
    border
  " data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block link-gray no-underline js-toggle-user-status-edit toggle-user-status-edit "
      role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:34841791,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:34841791,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;}}" data-hydro-click-hmac="e2f4b4953de77054a92d19a3e68d08166f6dfa37a98afb7d171ea30190eb631d">
      <div class="d-flex">
        <div class="f6 lh-condensed user-status-header
          d-inline-block v-align-middle
            user-status-emoji-only-header circle
            pr-2
"
            style="max-width: 29px"
          >
          <div class="user-status-emoji-container flex-shrink-0 mr-1 mt-1 lh-condensed-ultra v-align-bottom" style="">
            <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.5 8C1.5 6.27609 2.18482 4.62279 3.40381 3.40381C4.62279 2.18482 6.27609 1.5 8 1.5C9.72391 1.5 11.3772 2.18482 12.5962 3.40381C13.8152 4.62279 14.5 6.27609 14.5 8C14.5 9.72391 13.8152 11.3772 12.5962 12.5962C11.3772 13.8152 9.72391 14.5 8 14.5C6.27609 14.5 4.62279 13.8152 3.40381 12.5962C2.18482 11.3772 1.5 9.72391 1.5 8ZM8 0C5.87827 0 3.84344 0.842855 2.34315 2.34315C0.842855 3.84344 0 5.87827 0 8C0 10.1217 0.842855 12.1566 2.34315 13.6569C3.84344 15.1571 5.87827 16 8 16C10.1217 16 12.1566 15.1571 13.6569 13.6569C15.1571 12.1566 16 10.1217 16 8C16 5.87827 15.1571 3.84344 13.6569 2.34315C12.1566 0.842855 10.1217 0 8 0V0ZM5 8C5.26522 8 5.51957 7.89464 5.70711 7.70711C5.89464 7.51957 6 7.26522 6 7C6 6.73478 5.89464 6.48043 5.70711 6.29289C5.51957 6.10536 5.26522 6 5 6C4.73478 6 4.48043 6.10536 4.29289 6.29289C4.10536 6.48043 4 6.73478 4 7C4 7.26522 4.10536 7.51957 4.29289 7.70711C4.48043 7.89464 4.73478 8 5 8ZM12 7C12 7.26522 11.8946 7.51957 11.7071 7.70711C11.5196 7.89464 11.2652 8 11 8C10.7348 8 10.4804 7.89464 10.2929 7.70711C10.1054 7.51957 10 7.26522 10 7C10 6.73478 10.1054 6.48043 10.2929 6.29289C10.4804 6.10536 10.7348 6 11 6C11.2652 6 11.5196 6.10536 11.7071 6.29289C11.8946 6.48043 12 6.73478 12 7ZM5.32 9.636C5.48134 9.52303 5.68064 9.47806 5.87486 9.51081C6.06908 9.54355 6.24262 9.65138 6.358 9.811L6.365 9.82C6.46785 9.93795 6.58549 10.0421 6.715 10.13C6.979 10.308 7.398 10.5 8 10.5C8.602 10.5 9.02 10.308 9.285 10.129C9.41451 10.0411 9.53215 9.93695 9.635 9.819L9.642 9.811C9.75737 9.64895 9.93239 9.53937 10.1285 9.50637C10.3247 9.47336 10.526 9.51963 10.688 9.635C10.85 9.75037 10.9596 9.92539 10.9926 10.1215C11.0256 10.3177 10.9794 10.519 10.864 10.681L10.25 10.25C10.864 10.68 10.864 10.681 10.863 10.681V10.682L10.862 10.684L10.86 10.687L10.855 10.694L10.841 10.713C10.7848 10.7883 10.7233 10.8594 10.657 10.926C10.4963 11.0924 10.3187 11.2415 10.127 11.371C9.49722 11.7894 8.75607 12.0086 8 12C7.054 12 6.348 11.692 5.874 11.37C5.62319 11.2003 5.39676 10.9971 5.201 10.766C5.1867 10.7486 5.1727 10.7309 5.159 10.713L5.145 10.693L5.14 10.687L5.138 10.684V10.682H5.137L5.75 10.25L5.136 10.68C5.02196 10.5172 4.97718 10.3159 5.01149 10.1201C5.04581 9.92439 5.1564 9.75027 5.319 9.636H5.32Z"></path></svg>
          </div>
        </div>
        <div class="
          d-inline-block v-align-middle
          
          
           css-truncate css-truncate-target 
           user-status-message-wrapper f6"
           style="line-height: 20px;" >
          <div class="d-inline-block text-gray-dark v-align-text-top text-left">
              <span class="text-gray ml-2">Set status</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="Clp4lLOFlCtiny79MlmXDDL9Gh1M44cPfFC3xn5BBxACCEscAr9pJYJUMx0SH7ee1RzNkGtQBvckIni1s0Yhug==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.72 3.72C3.86062 3.57955 4.05125 3.50066 4.25 3.50066C4.44875 3.50066 4.63937 3.57955 4.78 3.72L8 6.94L11.22 3.72C11.2887 3.64631 11.3715 3.58721 11.4635 3.54622C11.5555 3.50523 11.6548 3.48319 11.7555 3.48141C11.8562 3.47963 11.9562 3.49816 12.0496 3.53588C12.143 3.5736 12.2278 3.62974 12.299 3.70096C12.3703 3.77218 12.4264 3.85702 12.4641 3.9504C12.5018 4.04379 12.5204 4.14382 12.5186 4.24452C12.5168 4.34523 12.4948 4.44454 12.4538 4.53654C12.4128 4.62854 12.3537 4.71134 12.28 4.78L9.06 8L12.28 11.22C12.3537 11.2887 12.4128 11.3715 12.4538 11.4635C12.4948 11.5555 12.5168 11.6548 12.5186 11.7555C12.5204 11.8562 12.5018 11.9562 12.4641 12.0496C12.4264 12.143 12.3703 12.2278 12.299 12.299C12.2278 12.3703 12.143 12.4264 12.0496 12.4641C11.9562 12.5018 11.8562 12.5204 11.7555 12.5186C11.6548 12.5168 11.5555 12.4948 11.4635 12.4538C11.3715 12.4128 11.2887 12.3537 11.22 12.28L8 9.06L4.78 12.28C4.63782 12.4125 4.44977 12.4846 4.25547 12.4812C4.06117 12.4777 3.87579 12.399 3.73837 12.2616C3.60096 12.1242 3.52225 11.9388 3.51882 11.7445C3.51539 11.5502 3.58752 11.3622 3.72 11.22L6.94 8L3.72 4.78C3.57955 4.63938 3.50066 4.44875 3.50066 4.25C3.50066 4.05125 3.57955 3.86063 3.72 3.72Z"></path></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value="">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker btn-open-emoji-picker p-0">
                  <span class="js-user-status-original-emoji" hidden></span>
                  <span class="js-user-status-custom-emoji"></span>
                  <span class="js-user-status-no-emoji-icon" >
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.5 8C1.5 6.27609 2.18482 4.62279 3.40381 3.40381C4.62279 2.18482 6.27609 1.5 8 1.5C9.72391 1.5 11.3772 2.18482 12.5962 3.40381C13.8152 4.62279 14.5 6.27609 14.5 8C14.5 9.72391 13.8152 11.3772 12.5962 12.5962C11.3772 13.8152 9.72391 14.5 8 14.5C6.27609 14.5 4.62279 13.8152 3.40381 12.5962C2.18482 11.3772 1.5 9.72391 1.5 8ZM8 0C5.87827 0 3.84344 0.842855 2.34315 2.34315C0.842855 3.84344 0 5.87827 0 8C0 10.1217 0.842855 12.1566 2.34315 13.6569C3.84344 15.1571 5.87827 16 8 16C10.1217 16 12.1566 15.1571 13.6569 13.6569C15.1571 12.1566 16 10.1217 16 8C16 5.87827 15.1571 3.84344 13.6569 2.34315C12.1566 0.842855 10.1217 0 8 0V0ZM5 8C5.26522 8 5.51957 7.89464 5.70711 7.70711C5.89464 7.51957 6 7.26522 6 7C6 6.73478 5.89464 6.48043 5.70711 6.29289C5.51957 6.10536 5.26522 6 5 6C4.73478 6 4.48043 6.10536 4.29289 6.29289C4.10536 6.48043 4 6.73478 4 7C4 7.26522 4.10536 7.51957 4.29289 7.70711C4.48043 7.89464 4.73478 8 5 8ZM12 7C12 7.26522 11.8946 7.51957 11.7071 7.70711C11.5196 7.89464 11.2652 8 11 8C10.7348 8 10.4804 7.89464 10.2929 7.70711C10.1054 7.51957 10 7.26522 10 7C10 6.73478 10.1054 6.48043 10.2929 6.29289C10.4804 6.10536 10.7348 6 11 6C11.2652 6 11.5196 6.10536 11.7071 6.29289C11.8946 6.48043 12 6.73478 12 7ZM5.32 9.636C5.48134 9.52303 5.68064 9.47806 5.87486 9.51081C6.06908 9.54355 6.24262 9.65138 6.358 9.811L6.365 9.82C6.46785 9.93795 6.58549 10.0421 6.715 10.13C6.979 10.308 7.398 10.5 8 10.5C8.602 10.5 9.02 10.308 9.285 10.129C9.41451 10.0411 9.53215 9.93695 9.635 9.819L9.642 9.811C9.75737 9.64895 9.93239 9.53937 10.1285 9.50637C10.3247 9.47336 10.526 9.51963 10.688 9.635C10.85 9.75037 10.9596 9.92539 10.9926 10.1215C11.0256 10.3177 10.9794 10.519 10.864 10.681L10.25 10.25C10.864 10.68 10.864 10.681 10.863 10.681V10.682L10.862 10.684L10.86 10.687L10.855 10.694L10.841 10.713C10.7848 10.7883 10.7233 10.8594 10.657 10.926C10.4963 11.0924 10.3187 11.2415 10.127 11.371C9.49722 11.7894 8.75607 12.0086 8 12C7.054 12 6.348 11.692 5.874 11.37C5.62319 11.2003 5.39676 10.9971 5.201 10.766C5.1867 10.7486 5.1727 10.7309 5.159 10.713L5.145 10.693L5.14 10.687L5.138 10.684V10.682H5.137L5.75 10.25L5.136 10.68C5.02196 10.5172 4.97718 10.3159 5.01149 10.1201C5.04581 9.92439 5.1564 9.75027 5.319 9.636H5.32Z"></path></svg>
                  </span>
                </button>
              </span>
              <text-expander keys=": @" data-mention-url="/autocomplete/user-suggestions" data-emoji-url="/autocomplete/emoji">
                <input
                  type="text"
                  autocomplete="off"
                  data-no-org-url="/autocomplete/user-suggestions"
                  data-org-url="/suggestions?mention_suggester=1"
                  data-maxlength="80"
                  class="d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field"
                  placeholder="What's happening?"
                  name="message"
                  value=""
                  aria-label="What is your current status?">
              </text-expander>
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true-compact-true" id="limited-availability-truncate-true-compact-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true-compact-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true-compact-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
          <div class="d-inline-block f5 mr-2 pt-3 pb-2" >
  <div class="d-inline-block mr-1">
    Clear status
  </div>

  <details class="js-user-status-expire-drop-down f6 dropdown details-reset details-overlay d-inline-block mr-2">
    <summary class="f5 btn-link link-gray-dark border px-2 py-1 rounded-1" aria-haspopup="true">
      <div class="js-user-status-expiration-interval-selected d-inline-block v-align-baseline">
        Never
      </div>
      <div class="dropdown-caret"></div>
    </summary>

    <ul class="dropdown-menu dropdown-menu-se pl-0 overflow-auto" style="width: 220px; max-height: 15.5em">
      <li>
        <button type="button" class="btn-link dropdown-item js-user-status-expire-button ws-normal" title="Never">
          <span class="d-inline-block text-bold mb-1">Never</span>
          <div class="f6 lh-condensed">Keep this status until you clear your status or edit your status.</div>
        </button>
      </li>
      <li class="dropdown-divider" role="none"></li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 30 minutes" value="2020-06-05T13:13:08+02:00">
            in 30 minutes
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 1 hour" value="2020-06-05T13:43:08+02:00">
            in 1 hour
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 4 hours" value="2020-06-05T16:43:08+02:00">
            in 4 hours
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="today" value="2020-06-05T23:59:59+02:00">
            today
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="this week" value="2020-06-07T23:59:59+02:00">
            this week
          </button>
        </li>
    </ul>
  </details>
  <input class="js-user-status-expiration-date-input" type="hidden" name="expires_at" value="">
</div>

          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit" disabled class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button" disabled class="width-full js-clear-user-status-button btn ml-2 ">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

      </div>
      <div role="none" class="dropdown-divider"></div>

    <a role="menuitem" class="dropdown-item" href="/raulbenitez" data-ga-click="Header, go to profile, text:your profile">Your profile</a>

    <a role="menuitem" class="dropdown-item" href="/raulbenitez?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a>


    <a role="menuitem" class="dropdown-item" href="/raulbenitez?tab=projects" data-ga-click="Header, go to projects, text:your projects">Your projects</a>

    <a role="menuitem" class="dropdown-item" href="/raulbenitez?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a>
      <a role="menuitem" class="dropdown-item" href="https://gist.github.com/mine" data-ga-click="Header, your gists, text:your gists">Your gists</a>





    <div role="none" class="dropdown-divider"></div>
      
<div id="feature-enrollment-toggle" class="hide-sm hide-md feature-preview-details position-relative">
  <button
    type="button"
    class="dropdown-item btn-link"
    role="menuitem"
    data-feature-preview-trigger-url="/users/raulbenitez/feature_previews"
    data-feature-preview-close-details="{&quot;event_type&quot;:&quot;feature_preview.clicks.close_modal&quot;,&quot;payload&quot;:{&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}"
    data-feature-preview-close-hmac="1f6e8b4f2a74f9ebf4f793c836728b507f72fa939a298154e62c126bc80857ea"
    data-hydro-click="{&quot;event_type&quot;:&quot;feature_preview.clicks.open_modal&quot;,&quot;payload&quot;:{&quot;link_location&quot;:&quot;user_dropdown&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}"
    data-hydro-click-hmac="ebc14639a6e6dc0e49456be67f6fd3da6cf642fc2fefee245a72bcde7bb9773a"
  >
    Feature preview
  </button>
    <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
</div>

    <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
    <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="F6W/gVaIFvSByEb0cozVQ9+kkxjtddgvai/idultSldYz4nFxS8RnwTk52blaCJK5Iy5ptMEAMd67tvn60a7ww==" />
      
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
        Sign out
      </button>
      <input type="text" name="required_field_72f4" hidden="hidden" class="form-control" /><input type="hidden" name="timestamp" value="1591353788659" class="form-control" /><input type="hidden" name="timestamp_secret" value="879e4364fa0122ef1884f9e2325f197a0b6fd1ecf23c7ad2dfb6b6bea7a3353a" class="form-control" />
</form>  </details-menu>
</details>

  </div>

</header>

        

    </div>

  <div id="start-of-content" class="show-on-focus"></div>




    <div id="js-flash-container">


  <template class="js-flash-template">
    <div class="flash flash-full  js-flash-template-container">
  <div class="container-lg px-2" >
    <button class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.72 3.72C3.86062 3.57955 4.05125 3.50066 4.25 3.50066C4.44875 3.50066 4.63937 3.57955 4.78 3.72L8 6.94L11.22 3.72C11.2887 3.64631 11.3715 3.58721 11.4635 3.54622C11.5555 3.50523 11.6548 3.48319 11.7555 3.48141C11.8562 3.47963 11.9562 3.49816 12.0496 3.53588C12.143 3.5736 12.2278 3.62974 12.299 3.70096C12.3703 3.77218 12.4264 3.85702 12.4641 3.9504C12.5018 4.04379 12.5204 4.14382 12.5186 4.24452C12.5168 4.34523 12.4948 4.44454 12.4538 4.53654C12.4128 4.62854 12.3537 4.71134 12.28 4.78L9.06 8L12.28 11.22C12.3537 11.2887 12.4128 11.3715 12.4538 11.4635C12.4948 11.5555 12.5168 11.6548 12.5186 11.7555C12.5204 11.8562 12.5018 11.9562 12.4641 12.0496C12.4264 12.143 12.3703 12.2278 12.299 12.299C12.2278 12.3703 12.143 12.4264 12.0496 12.4641C11.9562 12.5018 11.8562 12.5204 11.7555 12.5186C11.6548 12.5168 11.5555 12.4948 11.4635 12.4538C11.3715 12.4128 11.2887 12.3537 11.22 12.28L8 9.06L4.78 12.28C4.63782 12.4125 4.44977 12.4846 4.25547 12.4812C4.06117 12.4777 3.87579 12.399 3.73837 12.2616C3.60096 12.1242 3.52225 11.9388 3.51882 11.7445C3.51539 11.5502 3.58752 11.3622 3.72 11.22L6.94 8L3.72 4.78C3.57955 4.63938 3.50066 4.44875 3.50066 4.25C3.50066 4.05125 3.57955 3.86063 3.72 3.72Z"></path></svg>
    </button>
    
      <div class="js-flash-template-message"></div>

  </div>
</div>
  </template>
</div>


      

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>




  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      

  












  <div class="pagehead repohead hx_repohead readability-menu bg-gray-light pb-0 pt-0 pt-lg-3">

    <div class="d-flex container-lg mb-4 p-responsive d-none d-lg-flex">

      <div class="flex-auto min-width-0 width-fit mr-3">
        <h1 class="public  d-flex flex-wrap flex-items-center break-word float-none ">
  <span class="flex-self-stretch" style="margin-top: -2px;">
      <svg class="octicon octicon-repo" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M2 2.5C2 1.83696 2.26339 1.20107 2.73223 0.732233C3.20108 0.263392 3.83696 0 4.5 0L13.25 0C13.4489 0 13.6397 0.0790176 13.7803 0.21967C13.921 0.360322 14 0.551088 14 0.75V13.25C14 13.4489 13.921 13.6397 13.7803 13.7803C13.6397 13.921 13.4489 14 13.25 14H10.75C10.5511 14 10.3603 13.921 10.2197 13.7803C10.079 13.6397 10 13.4489 10 13.25C10 13.0511 10.079 12.8603 10.2197 12.7197C10.3603 12.579 10.5511 12.5 10.75 12.5H12.5V10.5H4.5C4.30308 10.5 4.11056 10.5582 3.94657 10.6672C3.78257 10.7762 3.65442 10.9312 3.57816 11.1128C3.50191 11.2943 3.48096 11.4943 3.51793 11.6878C3.5549 11.8812 3.64816 12.0594 3.786 12.2C3.92524 12.3422 4.0023 12.5338 4.00024 12.7328C3.99818 12.9318 3.91716 13.1218 3.775 13.261C3.63285 13.4002 3.4412 13.4773 3.24222 13.4752C3.04325 13.4732 2.85324 13.3922 2.714 13.25C2.25571 12.7829 1.99929 12.1544 2 11.5V2.5ZM12.5 1.5V9H4.5C4.144 9 3.806 9.074 3.5 9.208V2.5C3.5 2.23478 3.60536 1.98043 3.79289 1.79289C3.98043 1.60536 4.23478 1.5 4.5 1.5H12.5ZM5 12.25V15.5C5 15.5464 5.01293 15.5919 5.03734 15.6314C5.06175 15.6709 5.09667 15.7028 5.1382 15.7236C5.17972 15.7444 5.22621 15.7532 5.27245 15.749C5.31869 15.7448 5.36286 15.7279 5.4 15.7L6.85 14.613C6.89328 14.5805 6.94591 14.563 7 14.563C7.05409 14.563 7.10673 14.5805 7.15 14.613L8.6 15.7C8.63714 15.7279 8.68131 15.7448 8.72755 15.749C8.77379 15.7532 8.82028 15.7444 8.8618 15.7236C8.90333 15.7028 8.93826 15.6709 8.96266 15.6314C8.98707 15.5919 9 15.5464 9 15.5V12.25C9 12.1837 8.97366 12.1201 8.92678 12.0732C8.87989 12.0263 8.81631 12 8.75 12H5.25C5.1837 12 5.12011 12.0263 5.07322 12.0732C5.02634 12.1201 5 12.1837 5 12.25Z"></path></svg>
  </span>
  <span class="author ml-2 flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/users/raulbenitez/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/raulbenitez">raulbenitez</a>
  </span>
  <span class="path-divider flex-self-stretch">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#js-repo-pjax-container" href="/raulbenitez/MITO_FIBERS">MITO_FIBERS</a>
  </strong>
  
</h1>


      </div>

      <ul class="pagehead-actions flex-shrink-0 " >




  <li>
    
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="clearfix js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="PfNaeqLDe4u1W7RkMTaG4OOwI/3KvsK6ID6dwUQL286HrJf0Wbb6TqD4OKrdE/IpvIna0cfpVfQ92UBEwIKB9g==" />      <input type="hidden" name="repository_id" value="265504996">

      <details class="details-reset details-overlay select-menu float-left" >
        <summary class="select-menu-button float-left btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:265504996,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="c1f8960565b6eec062d555bf4c5eda8bd676423f8951affece9a679f60f97e97" data-ga-click="Repository, click Watch settings, action:blob#show">          <span data-menu-button>
              <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.67884 7.93165C2.09143 7.31094 2.9206 6.18152 4.0447 5.21477C5.17567 4.2421 6.52738 3.5 8.00001 3.5C9.47264 3.5 10.8244 4.2421 11.9553 5.21477C13.0794 6.18152 13.9086 7.31094 14.3212 7.93165C14.35 7.975 14.35 8.025 14.3212 8.06835C13.9086 8.68906 13.0794 9.81848 11.9553 10.7852C10.8244 11.7579 9.47264 12.5 8.00001 12.5C6.52738 12.5 5.17567 11.7579 4.0447 10.7852C2.9206 9.81848 2.09143 8.68906 1.67884 8.06835C1.65002 8.025 1.65002 7.975 1.67884 7.93165ZM8.00001 2C6.01865 2 4.32919 2.99167 3.06662 4.07751C1.79718 5.16926 0.880454 6.42307 0.429635 7.10129C0.0664231 7.64771 0.0664245 8.35229 0.429635 8.89871C0.880455 9.57693 1.79718 10.8307 3.06662 11.9225C4.32919 13.0083 6.01865 14 8.00001 14C9.98137 14 11.6708 13.0083 12.9334 11.9225C14.2028 10.8307 15.1196 9.57693 15.5704 8.89871C15.9336 8.35229 15.9336 7.64771 15.5704 7.10129C15.1196 6.42307 14.2028 5.16926 12.9334 4.07751C11.6708 2.99167 9.98137 2 8.00001 2ZM8 10C9.10457 10 10 9.10457 10 8C10 6.89543 9.10457 6 8 6C6.89543 6 6 6.89543 6 8C6 9.10457 6.89543 10 8 10Z"></path></svg>
              Unwatch
          </span>
</summary>        <details-menu
          class="select-menu-modal position-absolute mt-5"
          style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button
              type="submit"
              name="do"
              value="included"
              class="select-menu-item width-full"
              aria-checked="false"
              role="menuitemradio"
              
            >
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.67884 7.93165C2.09143 7.31094 2.9206 6.18152 4.0447 5.21477C5.17567 4.2421 6.52738 3.5 8.00001 3.5C9.47264 3.5 10.8244 4.2421 11.9553 5.21477C13.0794 6.18152 13.9086 7.31094 14.3212 7.93165C14.35 7.975 14.35 8.025 14.3212 8.06835C13.9086 8.68906 13.0794 9.81848 11.9553 10.7852C10.8244 11.7579 9.47264 12.5 8.00001 12.5C6.52738 12.5 5.17567 11.7579 4.0447 10.7852C2.9206 9.81848 2.09143 8.68906 1.67884 8.06835C1.65002 8.025 1.65002 7.975 1.67884 7.93165ZM8.00001 2C6.01865 2 4.32919 2.99167 3.06662 4.07751C1.79718 5.16926 0.880454 6.42307 0.429635 7.10129C0.0664231 7.64771 0.0664245 8.35229 0.429635 8.89871C0.880455 9.57693 1.79718 10.8307 3.06662 11.9225C4.32919 13.0083 6.01865 14 8.00001 14C9.98137 14 11.6708 13.0083 12.9334 11.9225C14.2028 10.8307 15.1196 9.57693 15.5704 8.89871C15.9336 8.35229 15.9336 7.64771 15.5704 7.10129C15.1196 6.42307 14.2028 5.16926 12.9334 4.07751C11.6708 2.99167 9.98137 2 8.00001 2ZM8 10C9.10457 10 10 9.10457 10 8C10 6.89543 9.10457 6 8 6C6.89543 6 6 6.89543 6 8C6 9.10457 6.89543 10 8 10Z"></path></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.67884 7.93165C2.09143 7.31094 2.9206 6.18152 4.0447 5.21477C5.17567 4.2421 6.52738 3.5 8.00001 3.5C9.47264 3.5 10.8244 4.2421 11.9553 5.21477C13.0794 6.18152 13.9086 7.31094 14.3212 7.93165C14.35 7.975 14.35 8.025 14.3212 8.06835C13.9086 8.68906 13.0794 9.81848 11.9553 10.7852C10.8244 11.7579 9.47264 12.5 8.00001 12.5C6.52738 12.5 5.17567 11.7579 4.0447 10.7852C2.9206 9.81848 2.09143 8.68906 1.67884 8.06835C1.65002 8.025 1.65002 7.975 1.67884 7.93165ZM8.00001 2C6.01865 2 4.32919 2.99167 3.06662 4.07751C1.79718 5.16926 0.880454 6.42307 0.429635 7.10129C0.0664231 7.64771 0.0664245 8.35229 0.429635 8.89871C0.880455 9.57693 1.79718 10.8307 3.06662 11.9225C4.32919 13.0083 6.01865 14 8.00001 14C9.98137 14 11.6708 13.0083 12.9334 11.9225C14.2028 10.8307 15.1196 9.57693 15.5704 8.89871C15.9336 8.35229 15.9336 7.64771 15.5704 7.10129C15.1196 6.42307 14.2028 5.16926 12.9334 4.07751C11.6708 2.99167 9.98137 2 8.00001 2ZM8 10C9.10457 10 10 9.10457 10 8C10 6.89543 9.10457 6 8 6C6.89543 6 6 6.89543 6 8C6 9.10457 6.89543 10 8 10Z"></path></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.67884 7.93165C2.09143 7.31094 2.9206 6.18152 4.0447 5.21477C5.17567 4.2421 6.52738 3.5 8.00001 3.5C9.47264 3.5 10.8244 4.2421 11.9553 5.21477C13.0794 6.18152 13.9086 7.31094 14.3212 7.93165C14.35 7.975 14.35 8.025 14.3212 8.06835C13.9086 8.68906 13.0794 9.81848 11.9553 10.7852C10.8244 11.7579 9.47264 12.5 8.00001 12.5C6.52738 12.5 5.17567 11.7579 4.0447 10.7852C2.9206 9.81848 2.09143 8.68906 1.67884 8.06835C1.65002 8.025 1.65002 7.975 1.67884 7.93165ZM8.00001 2C6.01865 2 4.32919 2.99167 3.06662 4.07751C1.79718 5.16926 0.880454 6.42307 0.429635 7.10129C0.0664231 7.64771 0.0664245 8.35229 0.429635 8.89871C0.880455 9.57693 1.79718 10.8307 3.06662 11.9225C4.32919 13.0083 6.01865 14 8.00001 14C9.98137 14 11.6708 13.0083 12.9334 11.9225C14.2028 10.8307 15.1196 9.57693 15.5704 8.89871C15.9336 8.35229 15.9336 7.64771 15.5704 7.10129C15.1196 6.42307 14.2028 5.16926 12.9334 4.07751C11.6708 2.99167 9.98137 2 8.00001 2ZM8 10C9.10457 10 10 9.10457 10 8C10 6.89543 9.10457 6 8 6C6.89543 6 6 6.89543 6 8C6 9.10457 6.89543 10 8 10Z"></path></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-bell-slash" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.00005 1.5C7.00314 1.5 6.1046 1.91582 5.4662 2.58554C5.1804 2.88536 4.70566 2.89673 4.40584 2.61093C4.10602 2.32513 4.09465 1.85039 4.38045 1.55057C5.29016 0.596222 6.5761 0 8.00005 0C10.7615 0 13.0001 2.23858 13.0001 5V7.37362C13.0001 7.78783 12.6643 8.12362 12.2501 8.12362C11.8358 8.12362 11.5001 7.78783 11.5001 7.37362V5C11.5001 3.067 9.93305 1.5 8.00005 1.5ZM4.1824 4.3095L1.18994 2.14254C0.854447 1.8996 0.385538 1.97462 0.142598 2.31011C-0.100343 2.6456 -0.0253172 3.11451 0.310172 3.35745L3.00005 5.30529V7.94722C3.00005 7.99658 2.98544 8.04483 2.95807 8.0859L1.25493 10.6406C1.08874 10.8899 1.00005 11.1828 1.00005 11.4824C1.00005 12.3206 1.6795 13 2.51765 13H13.6261L14.8102 13.8574C15.1457 14.1004 15.6146 14.0254 15.8575 13.6899C16.1005 13.3544 16.0254 12.8855 15.6899 12.6425L14.3154 11.6472C14.3108 11.6438 14.3062 11.6405 14.3016 11.6372L4.19778 4.32063C4.1927 4.31686 4.18758 4.31314 4.1824 4.3095ZM11.5546 11.5L4.50005 6.3915V7.94722C4.50005 8.29272 4.39779 8.63048 4.20614 8.91795L2.50301 11.4726C2.50108 11.4755 2.50005 11.4789 2.50005 11.4824C2.50005 11.4862 2.50068 11.488 2.50113 11.489C2.50179 11.4906 2.50307 11.4927 2.50521 11.4948C2.50734 11.497 2.50947 11.4983 2.51103 11.4989C2.51209 11.4994 2.51383 11.5 2.51765 11.5H11.5546ZM8.00005 16C9.02013 16 9.86184 15.2363 9.98464 14.2495C10.0017 14.1125 9.88812 14 9.75005 14H6.25005C6.11198 14 5.99841 14.1125 6.01546 14.2495C6.13827 15.2363 6.97998 16 8.00005 16Z"></path></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
        <a class="social-count js-social-count"
          href="/raulbenitez/MITO_FIBERS/watchers"
          aria-label="1 user is watching this repository">
          1
        </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <form class="starred js-social-form" action="/raulbenitez/MITO_FIBERS/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="P4BIZhyJovWtC653EDqCv4bWDmQuiaC2oAcZDl4FfMGvKaNaX5gdZcWfsCAoM2UulSqxVa5r0iBVsoUb0QTFPA==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count  js-toggler-target" aria-label="Unstar this repository" title="Unstar raulbenitez/MITO_FIBERS" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:265504996,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="2f62b2b3dfd9e07cc5e3c38035b4d85672b9f37cf44a9647de48197986ff3c81" data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">        <svg height="16" class="octicon octicon-star-fill" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8 0.25C8.14001 0.24991 8.27725 0.289014 8.39619 0.362887C8.51513 0.43676 8.61102 0.542452 8.673 0.668L10.555 4.483L14.765 5.095C14.9035 5.11511 15.0335 5.17355 15.1405 5.26372C15.2475 5.35388 15.3271 5.47218 15.3704 5.60523C15.4137 5.73829 15.4189 5.8808 15.3854 6.01665C15.3519 6.1525 15.2811 6.27628 15.181 6.374L12.135 9.344L12.854 13.536C12.8777 13.6739 12.8624 13.8157 12.8097 13.9454C12.757 14.0751 12.6691 14.1874 12.5559 14.2697C12.4427 14.352 12.3087 14.401 12.1691 14.4111C12.0295 14.4212 11.8899 14.3921 11.766 14.327L8 12.347L4.234 14.327C4.11018 14.392 3.97066 14.4211 3.83119 14.411C3.69171 14.4009 3.55784 14.352 3.44468 14.2699C3.33152 14.1877 3.24359 14.0755 3.19081 13.946C3.13803 13.8165 3.12251 13.6749 3.146 13.537L3.866 9.343L0.817997 6.374C0.717563 6.27632 0.646496 6.15247 0.612848 6.01647C0.579201 5.88047 0.584318 5.73777 0.627621 5.60453C0.670924 5.47129 0.75068 5.35284 0.857852 5.26261C0.965025 5.17238 1.09533 5.11397 1.234 5.094L5.444 4.483L7.327 0.668C7.38898 0.542452 7.48486 0.43676 7.6038 0.362887C7.72274 0.289014 7.85998 0.24991 8 0.25Z"></path></svg>

        Unstar
</button>        <a class="social-count js-social-count" href="/raulbenitez/MITO_FIBERS/stargazers"
           aria-label="0 users starred this repository">
           0
        </a>
</form>
    <form class="unstarred js-social-form" action="/raulbenitez/MITO_FIBERS/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="iJPsnYAFXXlORWauKVIfD5lvz6HCjZZfhxAd9o3p6rHeiA4zg8CXfgxVELLvFoVNmGSubwQUaOA3zzW1i3PpxQ==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count  js-toggler-target" aria-label="Unstar this repository" title="Star raulbenitez/MITO_FIBERS" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:265504996,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="72cb28c0e604e8bc814f9d80de7e5af7e00438f22e34aa4160cecbdb0aba8f82" data-ga-click="Repository, click star button, action:blob#show; text:Star">        <svg height="16" class="octicon octicon-star" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.00001 0.25C8.14003 0.24991 8.27727 0.289014 8.39621 0.362887C8.51515 0.43676 8.61103 0.542452 8.67301 0.668L10.555 4.483L14.765 5.095C14.9035 5.11511 15.0336 5.17355 15.1405 5.26372C15.2475 5.35388 15.3272 5.47218 15.3704 5.60523C15.4137 5.73829 15.4189 5.8808 15.3854 6.01665C15.352 6.1525 15.2812 6.27628 15.181 6.374L12.135 9.344L12.854 13.536C12.8777 13.6739 12.8624 13.8157 12.8097 13.9454C12.757 14.0751 12.6691 14.1874 12.5559 14.2697C12.4427 14.352 12.3087 14.401 12.1691 14.4111C12.0295 14.4212 11.8899 14.3921 11.766 14.327L8.00001 12.347L4.23401 14.327C4.1102 14.392 3.97068 14.4211 3.8312 14.411C3.69173 14.4009 3.55785 14.352 3.44469 14.2699C3.33154 14.1877 3.2436 14.0755 3.19083 13.946C3.13805 13.8165 3.12252 13.6749 3.14601 13.537L3.86601 9.343L0.818012 6.374C0.717578 6.27632 0.646511 6.15247 0.612864 6.01647C0.579216 5.88047 0.584334 5.73777 0.627636 5.60453C0.670939 5.47129 0.750695 5.35284 0.857868 5.26261C0.96504 5.17238 1.09534 5.11397 1.23401 5.094L5.44401 4.483L7.32701 0.668C7.38899 0.542452 7.48488 0.43676 7.60382 0.362887C7.72276 0.289014 7.86 0.24991 8.00001 0.25ZM8.00001 2.695L6.61501 5.5C6.56123 5.6089 6.4818 5.70311 6.38356 5.77453C6.28531 5.84595 6.17119 5.89244 6.05101 5.91L2.95401 6.36L5.19401 8.544C5.28116 8.62886 5.34637 8.73365 5.384 8.84933C5.42163 8.96501 5.43056 9.0881 5.41001 9.208L4.88201 12.292L7.65101 10.836C7.75864 10.7794 7.87842 10.7499 8.00001 10.7499C8.12161 10.7499 8.24138 10.7794 8.34901 10.836L11.119 12.292L10.589 9.208C10.5685 9.0881 10.5774 8.96501 10.615 8.84933C10.6527 8.73365 10.7179 8.62886 10.805 8.544L13.045 6.361L9.94901 5.911C9.82883 5.89344 9.71471 5.84695 9.61647 5.77553C9.51822 5.70411 9.4388 5.6099 9.38501 5.501L8.00001 2.694V2.695Z"></path></svg>

        Star
</button>        <a class="social-count js-social-count" href="/raulbenitez/MITO_FIBERS/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
          <div class="float-left">
            <details class="details-reset details-overlay details-overlay-dark" >
                    <summary
                  class="btn btn-sm btn-with-count"
                  title="Fork your own copy of raulbenitez/MITO_FIBERS to your account"
                  data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:265504996,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="6d2dca7fdd68cd24638c49cd676553ce65f6d4e8858fec99f4d27329145f3be9" data-ga-click="Repository, show fork modal, action:blob#show; text:Fork">
                  <svg class="octicon octicon-repo-forked" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M5 3.25001C5 3.44892 4.92099 3.63969 4.78033 3.78034C4.63968 3.92099 4.44892 4.00001 4.25 4.00001C4.05109 4.00001 3.86033 3.92099 3.71967 3.78034C3.57902 3.63969 3.5 3.44892 3.5 3.25001C3.5 3.05109 3.57902 2.86033 3.71967 2.71968C3.86033 2.57902 4.05109 2.50001 4.25 2.50001C4.44892 2.50001 4.63968 2.57902 4.78033 2.71968C4.92099 2.86033 5 3.05109 5 3.25001ZM5 5.37201C5.50042 5.19509 5.92217 4.84696 6.19073 4.38915C6.45929 3.93134 6.55735 3.39333 6.4676 2.87021C6.37785 2.34709 6.10605 1.87253 5.70025 1.53043C5.29445 1.18832 4.78077 1.00069 4.25 1.00069C3.71924 1.00069 3.20556 1.18832 2.79976 1.53043C2.39396 1.87253 2.12216 2.34709 2.03241 2.87021C1.94265 3.39333 2.04072 3.93134 2.30928 4.38915C2.57784 4.84696 2.99959 5.19509 3.5 5.37201V6.25001C3.5 6.84674 3.73706 7.41904 4.15901 7.841C4.58097 8.26295 5.15327 8.50001 5.75 8.50001H7.25V10.628C6.74932 10.8049 6.3273 11.1532 6.05855 11.6112C5.78981 12.0692 5.69164 12.6075 5.78139 13.1309C5.87115 13.6543 6.14306 14.1291 6.54905 14.4714C6.95504 14.8136 7.46897 15.0014 8 15.0014C8.53104 15.0014 9.04497 14.8136 9.45096 14.4714C9.85695 14.1291 10.1289 13.6543 10.2186 13.1309C10.3084 12.6075 10.2102 12.0692 9.94146 11.6112C9.67271 11.1532 9.25069 10.8049 8.75 10.628V8.50001H10.25C10.8467 8.50001 11.419 8.26295 11.841 7.841C12.263 7.41904 12.5 6.84674 12.5 6.25001V5.37201C13.0004 5.19509 13.4222 4.84696 13.6907 4.38915C13.9593 3.93134 14.0574 3.39333 13.9676 2.87021C13.8778 2.34709 13.6061 1.87253 13.2002 1.53043C12.7944 1.18832 12.2808 1.00069 11.75 1.00069C11.2192 1.00069 10.7056 1.18832 10.2998 1.53043C9.89396 1.87253 9.62216 2.34709 9.53241 2.87021C9.44265 3.39333 9.54072 3.93134 9.80928 4.38915C10.0778 4.84696 10.4996 5.19509 11 5.37201V6.25001C11 6.44892 10.921 6.63969 10.7803 6.78034C10.6397 6.92099 10.4489 7.00001 10.25 7.00001H5.75C5.55109 7.00001 5.36033 6.92099 5.21967 6.78034C5.07902 6.63969 5 6.44892 5 6.25001V5.37201ZM8.75 12.75C8.75 12.9489 8.67099 13.1397 8.53033 13.2803C8.38968 13.421 8.19892 13.5 8 13.5C7.80109 13.5 7.61033 13.421 7.46967 13.2803C7.32902 13.1397 7.25 12.9489 7.25 12.75C7.25 12.5511 7.32902 12.3603 7.46967 12.2197C7.61033 12.079 7.80109 12 8 12C8.19892 12 8.38968 12.079 8.53033 12.2197C8.67099 12.3603 8.75 12.5511 8.75 12.75ZM11.75 4.00001C11.9489 4.00001 12.1397 3.92099 12.2803 3.78034C12.421 3.63969 12.5 3.44892 12.5 3.25001C12.5 3.05109 12.421 2.86033 12.2803 2.71968C12.1397 2.57902 11.9489 2.50001 11.75 2.50001C11.5511 2.50001 11.3603 2.57902 11.2197 2.71968C11.079 2.86033 11 3.05109 11 3.25001C11 3.44892 11.079 3.63969 11.2197 3.78034C11.3603 3.92099 11.5511 4.00001 11.75 4.00001Z"></path></svg>
                  Fork
                </summary>

  <details-dialog
    class="Box d-flex flex-column anim-fade-in fast Box--overlay"
      src="/raulbenitez/MITO_FIBERS/fork?fragment=1"
      preload
    >
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
        <svg height="16" class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.72 3.72C3.86062 3.57955 4.05125 3.50066 4.25 3.50066C4.44875 3.50066 4.63937 3.57955 4.78 3.72L8 6.94L11.22 3.72C11.2887 3.64631 11.3715 3.58721 11.4635 3.54622C11.5555 3.50523 11.6548 3.48319 11.7555 3.48141C11.8562 3.47963 11.9562 3.49816 12.0496 3.53588C12.143 3.5736 12.2278 3.62974 12.299 3.70096C12.3703 3.77218 12.4264 3.85702 12.4641 3.9504C12.5018 4.04379 12.5204 4.14382 12.5186 4.24452C12.5168 4.34523 12.4948 4.44454 12.4538 4.53654C12.4128 4.62854 12.3537 4.71134 12.28 4.78L9.06 8L12.28 11.22C12.3537 11.2887 12.4128 11.3715 12.4538 11.4635C12.4948 11.5555 12.5168 11.6548 12.5186 11.7555C12.5204 11.8562 12.5018 11.9562 12.4641 12.0496C12.4264 12.143 12.3703 12.2278 12.299 12.299C12.2278 12.3703 12.143 12.4264 12.0496 12.4641C11.9562 12.5018 11.8562 12.5204 11.7555 12.5186C11.6548 12.5168 11.5555 12.4948 11.4635 12.4538C11.3715 12.4128 11.2887 12.3537 11.22 12.28L8 9.06L4.78 12.28C4.63782 12.4125 4.44977 12.4846 4.25547 12.4812C4.06117 12.4777 3.87579 12.399 3.73837 12.2616C3.60096 12.1242 3.52225 11.9388 3.51882 11.7445C3.51539 11.5502 3.58752 11.3622 3.72 11.22L6.94 8L3.72 4.78C3.57955 4.63938 3.50066 4.44875 3.50066 4.25C3.50066 4.05125 3.57955 3.86063 3.72 3.72Z"></path></svg>

      </button>
      <h3 class="Box-title">Fork MITO_FIBERS</h3>
    </div>
      
              <div class="text-center overflow-auto">
                <include-fragment>
                  <div class="octocat-spinner my-5" aria-label="Loading..."></div>
                  <p class="f5 text-gray">If this dialog fails to load, you can visit <a href="/raulbenitez/MITO_FIBERS/fork">the fork page</a> directly.</p>
                </include-fragment>
              </div>

  </details-dialog>
</details>
          </div>

    <a href="/raulbenitez/MITO_FIBERS/network/members" class="social-count"
       aria-label="0 users forked this repository">
      0
    </a>
  </li>
</ul>

    </div>
      <nav class="js-repo-nav js-sidenav-container-pjax clearfix hx_reponav reponav p-responsive d-none d-lg-block container-lg"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">
  <ul class="list-style-none">
    <li  itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /raulbenitez/MITO_FIBERS" href="/raulbenitez/MITO_FIBERS">
        <div class="d-inline"><svg class="octicon octicon-code" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.71967 3.21967C5.01256 2.92678 5.48744 2.92678 5.78033 3.21967C6.07322 3.51256 6.07322 3.98744 5.78033 4.28033L2.06066 8L5.78033 11.7197C6.07322 12.0126 6.07322 12.4874 5.78033 12.7803C5.48744 13.0732 5.01256 13.0732 4.71967 12.7803L0.46967 8.53033C0.176777 8.23744 0.176777 7.76256 0.46967 7.46967L4.71967 3.21967ZM11.2803 3.21967C10.9874 2.92678 10.5126 2.92678 10.2197 3.21967C9.92678 3.51256 9.92678 3.98744 10.2197 4.28033L13.9393 8L10.2197 11.7197C9.92678 12.0126 9.92678 12.4874 10.2197 12.7803C10.5126 13.0732 10.9874 13.0732 11.2803 12.7803L15.5303 8.53033C15.8232 8.23744 15.8232 7.76256 15.5303 7.46967L11.2803 3.21967Z"></path></svg></div>
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </li>

      <li  itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /raulbenitez/MITO_FIBERS/issues" href="/raulbenitez/MITO_FIBERS/issues">
          <div class="d-inline"><svg class="octicon octicon-issue-opened" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8 1.5C6.27609 1.5 4.62279 2.18482 3.40381 3.40381C2.18482 4.62279 1.5 6.27609 1.5 8C1.5 9.72391 2.18482 11.3772 3.40381 12.5962C4.62279 13.8152 6.27609 14.5 8 14.5C9.72391 14.5 11.3772 13.8152 12.5962 12.5962C13.8152 11.3772 14.5 9.72391 14.5 8C14.5 6.27609 13.8152 4.62279 12.5962 3.40381C11.3772 2.18482 9.72391 1.5 8 1.5ZM0 8C0 5.87827 0.842855 3.84344 2.34315 2.34315C3.84344 0.842855 5.87827 0 8 0C10.1217 0 12.1566 0.842855 13.6569 2.34315C15.1571 3.84344 16 5.87827 16 8C16 10.1217 15.1571 12.1566 13.6569 13.6569C12.1566 15.1571 10.1217 16 8 16C5.87827 16 3.84344 15.1571 2.34315 13.6569C0.842855 12.1566 0 10.1217 0 8ZM9 11C9 11.2652 8.89464 11.5196 8.70711 11.7071C8.51957 11.8946 8.26522 12 8 12C7.73478 12 7.48043 11.8946 7.29289 11.7071C7.10536 11.5196 7 11.2652 7 11C7 10.7348 7.10536 10.4804 7.29289 10.2929C7.48043 10.1054 7.73478 10 8 10C8.26522 10 8.51957 10.1054 8.70711 10.2929C8.89464 10.4804 9 10.7348 9 11ZM8.75 4.75C8.75 4.55109 8.67098 4.36032 8.53033 4.21967C8.38968 4.07902 8.19891 4 8 4C7.80109 4 7.61032 4.07902 7.46967 4.21967C7.32902 4.36032 7.25 4.55109 7.25 4.75V8.25C7.25 8.44891 7.32902 8.63968 7.46967 8.78033C7.61032 8.92098 7.80109 9 8 9C8.19891 9 8.38968 8.92098 8.53033 8.78033C8.67098 8.63968 8.75 8.44891 8.75 8.25V4.75Z"></path></svg></div>
          <span itemprop="name">Issues</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="2">
</a>      </li>

    <li  itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a data-hotkey="g p" data-skip-pjax="true" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /raulbenitez/MITO_FIBERS/pulls" href="/raulbenitez/MITO_FIBERS/pulls">
        <div class="d-inline"><svg class="octicon octicon-git-pull-request" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M7.17674 3.07322L9.57318 0.676753C9.73068 0.51926 9.99996 0.630802 9.99996 0.853529V5.64642C9.99996 5.86915 9.73068 5.98069 9.57319 5.8232L7.17674 3.42677C7.07911 3.32914 7.07911 3.17085 7.17674 3.07322ZM3.75 2.5C3.33579 2.5 3 2.83579 3 3.25C3 3.66421 3.33579 4 3.75 4C4.16421 4 4.5 3.66421 4.5 3.25C4.5 2.83579 4.16421 2.5 3.75 2.5ZM1.5 3.25C1.5 2.00736 2.50736 1 3.75 1C4.99264 1 6 2.00736 6 3.25C6 4.22966 5.37389 5.06309 4.5 5.37197V10.628C5.37389 10.9369 6 11.7703 6 12.75C6 13.9926 4.99264 15 3.75 15C2.50736 15 1.5 13.9926 1.5 12.75C1.5 11.7703 2.12611 10.9369 3 10.628V5.37197C2.12611 5.06309 1.5 4.22966 1.5 3.25ZM11 2.5H10V4H11C11.5523 4 12 4.44772 12 5V10.628C11.1261 10.9369 10.5 11.7703 10.5 12.75C10.5 13.9926 11.5074 15 12.75 15C13.9926 15 15 13.9926 15 12.75C15 11.7703 14.3739 10.9369 13.5 10.628V5C13.5 3.61929 12.3807 2.5 11 2.5ZM12 12.75C12 12.3358 12.3358 12 12.75 12C13.1642 12 13.5 12.3358 13.5 12.75C13.5 13.1642 13.1642 13.5 12.75 13.5C12.3358 13.5 12 13.1642 12 12.75ZM3.75 12C3.33579 12 3 12.3358 3 12.75C3 13.1642 3.33579 13.5 3.75 13.5C4.16421 13.5 4.5 13.1642 4.5 12.75C4.5 12.3358 4.16421 12 3.75 12Z"></path></svg></div>
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="4">
</a>    </li>


      <li itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement" class="position-relative float-left ">
        <a data-hotkey="g w" data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="repo_actions /raulbenitez/MITO_FIBERS/actions" href="/raulbenitez/MITO_FIBERS/actions">
          <div class="d-inline"><svg class="octicon octicon-play" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.5 8C1.5 4.41015 4.41015 1.5 8 1.5C11.5899 1.5 14.5 4.41015 14.5 8C14.5 11.5899 11.5899 14.5 8 14.5C4.41015 14.5 1.5 11.5899 1.5 8ZM8 0C3.58172 0 0 3.58172 0 8C0 12.4183 3.58172 16 8 16C12.4183 16 16 12.4183 16 8C16 3.58172 12.4183 0 8 0ZM6.37862 5.22717C6.21199 5.1272 6 5.24722 6 5.44155V10.5585C6 10.7528 6.21199 10.8728 6.37862 10.7728L10.6427 8.21437C10.8045 8.11727 10.8045 7.88273 10.6427 7.78563L6.37862 5.22717Z"></path></svg></div>
          Actions
</a>
      </li>

      <li >
        <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /raulbenitez/MITO_FIBERS/projects" href="/raulbenitez/MITO_FIBERS/projects">
          <div class="d-inline"><svg class="octicon octicon-project" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.75 0C0.783502 0 0 0.783501 0 1.75V14.25C0 15.2165 0.783501 16 1.75 16H14.25C15.2165 16 16 15.2165 16 14.25V1.75C16 0.783502 15.2165 0 14.25 0H1.75ZM1.5 1.75C1.5 1.61193 1.61193 1.5 1.75 1.5H14.25C14.3881 1.5 14.5 1.61193 14.5 1.75V14.25C14.5 14.3881 14.3881 14.5 14.25 14.5H1.75C1.61193 14.5 1.5 14.3881 1.5 14.25V1.75ZM11.75 3C11.3358 3 11 3.33579 11 3.75V11.25C11 11.6642 11.3358 12 11.75 12C12.1642 12 12.5 11.6642 12.5 11.25V3.75C12.5 3.33579 12.1642 3 11.75 3ZM3.5 3.75C3.5 3.33579 3.83579 3 4.25 3C4.66421 3 5 3.33579 5 3.75V9.25C5 9.66421 4.66421 10 4.25 10C3.83579 10 3.5 9.66421 3.5 9.25V3.75ZM8 3C7.58579 3 7.25 3.33579 7.25 3.75V7.25C7.25 7.66421 7.58579 8 8 8C8.41421 8 8.75 7.66421 8.75 7.25V3.75C8.75 3.33579 8.41421 3 8 3Z"></path></svg></div>
          Projects
          <span class="Counter">0</span>
</a>      </li>

      <li >
        <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /raulbenitez/MITO_FIBERS/wiki" href="/raulbenitez/MITO_FIBERS/wiki">
          <div class="d-inline"><svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M0 1.75C0 1.33579 0.335786 1 0.75 1H5.00286C6.23012 1 7.31979 1.58958 8.00393 2.50106C8.68803 1.58962 9.77766 1 11.005 1H15.25C15.6642 1 16 1.33579 16 1.75V12.25C16 12.6642 15.6642 13 15.25 13H10.7426C10.1459 13 9.57361 13.2371 9.15165 13.659L8.53033 14.2803C8.23744 14.5732 7.76256 14.5732 7.46967 14.2803L6.84835 13.659C6.42639 13.2371 5.8541 13 5.25736 13H0.75C0.335786 13 0 12.6642 0 12.25V1.75ZM8.755 4.75C8.755 3.50736 9.76236 2.5 11.005 2.5H14.5V11.5H10.7426C10.0326 11.5 9.34339 11.7014 8.75124 12.0724L8.755 4.75ZM7.25124 12.074L7.255 7.00071L7.25285 4.74786C7.25167 3.50605 6.24466 2.5 5.00286 2.5H1.5V11.5H5.25736C5.96836 11.5 6.65854 11.7019 7.25124 12.074Z"></path></svg></div>
          Wiki
</a>      </li>

      <li >
        <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security overview alerts policy token_scanning code_scanning /raulbenitez/MITO_FIBERS/security" href="/raulbenitez/MITO_FIBERS/security">
          <div class="d-inline"><svg class="octicon octicon-shield" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M7.46664 0.133062C7.81355 0.0220518 8.18645 0.0220524 8.53336 0.133063L13.7834 1.81306C14.5082 2.045 15 2.71878 15 3.4798V6.99985C15 8.5659 14.6808 10.1823 13.6968 11.682C12.7137 13.1805 11.1116 14.4946 8.66493 15.5367C8.24091 15.7173 7.75909 15.7173 7.33508 15.5367C4.88836 14.4946 3.28631 13.1805 2.3032 11.682C1.31923 10.1823 1 8.5659 1 6.99985V3.4798C1 2.71878 1.49183 2.045 2.21664 1.81306L7.46664 0.133062ZM8.07619 1.5617C8.02664 1.54584 7.97336 1.54584 7.92381 1.5617L2.67381 3.2417C2.57026 3.27483 2.5 3.37109 2.5 3.4798V6.99985C2.5 8.35818 2.77465 9.66618 3.55737 10.8592C4.34094 12.0535 5.67838 13.2007 7.92287 14.1567C7.97134 14.1773 8.02866 14.1773 8.07713 14.1567C10.3216 13.2007 11.6591 12.0535 12.4426 10.8592C13.2253 9.66618 13.5 8.35818 13.5 6.99985V3.4798C13.5 3.37109 13.4297 3.27483 13.3262 3.2417L8.07619 1.5617ZM9 10.4999C9 11.0522 8.55228 11.4999 8 11.4999C7.44772 11.4999 7 11.0522 7 10.4999C7 9.94759 7.44772 9.49988 8 9.49988C8.55228 9.49988 9 9.94759 9 10.4999ZM8.75 4.74988C8.75 4.33566 8.41421 3.99988 8 3.99988C7.58579 3.99988 7.25 4.33566 7.25 4.74988V7.74988C7.25 8.16409 7.58579 8.49988 8 8.49988C8.41421 8.49988 8.75 8.16409 8.75 7.74988V4.74988Z"></path></svg></div>
          Security
              <span class="Counter js-security-tab-count" data-url="/raulbenitez/MITO_FIBERS/security/overall-count" hidden></span>
</a>      </li>

      <li >
        <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people /raulbenitez/MITO_FIBERS/pulse" href="/raulbenitez/MITO_FIBERS/pulse">
          <div class="d-inline"><svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.5 1.75C1.5 1.33579 1.16421 1 0.75 1C0.335786 1 0 1.33579 0 1.75V14.25C0 14.6642 0.335786 15 0.75 15H15.25C15.6642 15 16 14.6642 16 14.25C16 13.8358 15.6642 13.5 15.25 13.5H1.5V1.75ZM15.7803 4.28033C16.0732 3.98744 16.0732 3.51256 15.7803 3.21967C15.4874 2.92678 15.0126 2.92678 14.7197 3.21967L10 7.93934L7.53033 5.46967C7.23744 5.17678 6.76256 5.17678 6.46967 5.46967L3.21967 8.71967C2.92678 9.01256 2.92678 9.48744 3.21967 9.78033C3.51256 10.0732 3.98744 10.0732 4.28033 9.78033L7 7.06066L9.46967 9.53033C9.61032 9.67098 9.80109 9.75 10 9.75C10.1989 9.75 10.3897 9.67098 10.5303 9.53033L15.7803 4.28033Z"></path></svg></div>
          Insights
</a>      </li>

      <li >
        <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks integration_installations repo_keys_settings issue_template_editor secrets_settings key_links_settings repo_actions_settings notifications /raulbenitez/MITO_FIBERS/settings" href="/raulbenitez/MITO_FIBERS/settings">
          <div class="d-inline"><svg class="octicon octicon-gear" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M7.4288 1.52471C7.61685 1.50836 7.80736 1.5 8 1.5C8.19264 1.5 8.38315 1.50836 8.5712 1.52471C8.60669 1.52779 8.67932 1.56149 8.70795 1.67093L8.99702 2.77622C9.14363 3.33676 9.54617 3.74277 9.99429 3.96473C10.1678 4.05067 10.3351 4.14753 10.4952 4.25443C10.9118 4.53261 11.4652 4.67836 12.0243 4.52497L13.1272 4.22235C13.2361 4.19246 13.3017 4.23831 13.3223 4.26758C13.5408 4.57848 13.7326 4.90924 13.8946 5.25654C13.9094 5.2884 13.9167 5.36792 13.8362 5.44746L13.0214 6.25258C12.6099 6.65921 12.4591 7.21008 12.4908 7.70918C12.4969 7.80524 12.5 7.9022 12.5 8C12.5 8.0978 12.4969 8.19476 12.4908 8.29082C12.4591 8.78992 12.6099 9.34079 13.0214 9.74742L13.8362 10.5525C13.9167 10.6321 13.9094 10.7116 13.8946 10.7435C13.7326 11.0908 13.5408 11.4215 13.3223 11.7324C13.3017 11.7617 13.2361 11.8075 13.1272 11.7777L12.0243 11.475C11.4652 11.3216 10.9118 11.4674 10.4952 11.7456C10.3351 11.8525 10.1678 11.9493 9.99429 12.0353C9.54617 12.2572 9.14363 12.6632 8.99702 13.2238L8.70795 14.3291C8.67932 14.4385 8.60669 14.4722 8.5712 14.4753C8.38315 14.4916 8.19264 14.5 8 14.5C7.80736 14.5 7.61685 14.4916 7.4288 14.4753C7.3933 14.4722 7.32067 14.4385 7.29205 14.3291L7.00296 13.2237C6.85636 12.6632 6.45383 12.2572 6.00572 12.0353C5.83221 11.9493 5.66496 11.8525 5.50487 11.7456C5.08825 11.4674 4.53481 11.3216 3.97577 11.475L2.87278 11.7777C2.76387 11.8075 2.69826 11.7617 2.67768 11.7324C2.45921 11.4215 2.26738 11.0908 2.10543 10.7435C2.09057 10.7116 2.08328 10.6321 2.16377 10.5525L2.97865 9.74736C3.39017 9.34074 3.541 8.78987 3.50924 8.29078C3.50314 8.19474 3.50003 8.09778 3.50003 8C3.50003 7.90222 3.50314 7.80526 3.50924 7.70922C3.541 7.21013 3.39017 6.65926 2.97865 6.25264L2.16377 5.44746C2.08328 5.36793 2.09057 5.28841 2.10543 5.25655C2.26738 4.90924 2.45921 4.57848 2.67769 4.26758C2.69826 4.23831 2.76387 4.19247 2.87278 4.22235L3.97577 4.52498C4.53481 4.67837 5.08825 4.53262 5.50487 4.25444C5.66496 4.14755 5.83221 4.05069 6.00572 3.96475C6.45382 3.74279 6.85636 3.33678 7.00296 2.77625L7.29205 1.67093C7.32067 1.56149 7.3933 1.52779 7.4288 1.52471ZM8 0C7.76394 0 7.53009 0.010245 7.29889 0.0303435C6.55611 0.0949143 6.00991 0.645042 5.84086 1.29138L5.55177 2.39671C5.53431 2.46349 5.47287 2.55476 5.33993 2.62061C5.10832 2.73533 4.88526 2.86452 4.67192 3.00697C4.54894 3.08908 4.43933 3.09674 4.37267 3.07845L3.26968 2.77581C2.62644 2.59932 1.87827 2.79629 1.45041 3.40515C1.18168 3.78757 0.945496 4.19473 0.745967 4.62262C0.430999 5.29808 0.634823 6.04545 1.10948 6.51446L1.92436 7.31963C1.9735 7.36819 2.02164 7.46677 2.01227 7.61399C2.00415 7.74171 2.00003 7.87043 2.00003 8C2.00003 8.12957 2.00415 8.25829 2.01227 8.38601C2.02164 8.53323 1.9735 8.63181 1.92436 8.68037L1.10948 9.48555C0.634822 9.95455 0.430999 10.7019 0.745967 11.3774C0.945495 11.8053 1.18168 12.2124 1.45041 12.5948C1.87827 13.2037 2.62644 13.4007 3.26968 13.2242L4.37267 12.9216C4.43933 12.9033 4.54895 12.9109 4.67192 12.993C4.88526 13.1355 5.10832 13.2647 5.33993 13.3794C5.47287 13.4452 5.53431 13.5365 5.55177 13.6033L5.84086 14.7086C6.00991 15.355 6.55611 15.9051 7.29889 15.9697C7.53009 15.9898 7.76394 16 8 16C8.23606 16 8.46991 15.9898 8.7011 15.9697C9.44388 15.9051 9.99009 15.355 10.1591 14.7086L10.4482 13.6033C10.4657 13.5365 10.5271 13.4453 10.6601 13.3794C10.8917 13.2647 11.1148 13.1355 11.3281 12.993C11.4511 12.9109 11.5607 12.9033 11.6274 12.9216L12.7303 13.2242C13.3736 13.4007 14.1217 13.2037 14.5496 12.5949C14.8183 12.2124 15.0545 11.8053 15.254 11.3774C15.569 10.7019 15.3652 9.95456 14.8905 9.48555L14.0757 8.68042C14.0265 8.63187 13.9784 8.53328 13.9878 8.38606C13.9959 8.25832 14 8.12959 14 8C14 7.87041 13.9959 7.74168 13.9878 7.61394C13.9784 7.46672 14.0265 7.36813 14.0757 7.31958L14.8905 6.51445C15.3652 6.04544 15.569 5.29807 15.254 4.62261C15.0545 4.19472 14.8183 3.78756 14.5496 3.40515C14.1217 2.79628 13.3736 2.59932 12.7303 2.77581L11.6274 3.07843C11.5607 3.09672 11.4511 3.08907 11.3281 3.00696C11.1148 2.8645 10.8917 2.7353 10.6601 2.62057C10.5271 2.55473 10.4657 2.46346 10.4482 2.39667L10.1591 1.29138C9.99009 0.64504 9.44388 0.0949126 8.7011 0.0303426C8.46991 0.0102447 8.23606 0 8 0ZM9.5 8C9.5 8.82843 8.82843 9.5 8 9.5C7.17157 9.5 6.5 8.82843 6.5 8C6.5 7.17157 7.17157 6.5 8 6.5C8.82843 6.5 9.5 7.17157 9.5 8ZM11 8C11 9.65685 9.65685 11 8 11C6.34315 11 5 9.65685 5 8C5 6.34315 6.34315 5 8 5C9.65685 5 11 6.34315 11 8Z"></path></svg></div>
          Settings
</a>      </li>

  </ul>
</nav>

  <div class="reponav-wrapper reponav-small d-lg-none">
  <nav class="reponav js-reponav text-center no-wrap"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /raulbenitez/MITO_FIBERS" href="/raulbenitez/MITO_FIBERS">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /raulbenitez/MITO_FIBERS/issues" href="/raulbenitez/MITO_FIBERS/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="2">
</a>      </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /raulbenitez/MITO_FIBERS/pulls" href="/raulbenitez/MITO_FIBERS/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="4">
</a>    </span>


      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /raulbenitez/MITO_FIBERS/projects" href="/raulbenitez/MITO_FIBERS/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="5">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_actions /raulbenitez/MITO_FIBERS/actions" href="/raulbenitez/MITO_FIBERS/actions">
          <span itemprop="name">Actions</span>
          <meta itemprop="position" content="6">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_wiki /raulbenitez/MITO_FIBERS/wiki" href="/raulbenitez/MITO_FIBERS/wiki">
          <span itemprop="name">Wiki</span>
          <meta itemprop="position" content="7">
</a>      </span>

      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="security overview alerts policy token_scanning code_scanning /raulbenitez/MITO_FIBERS/security" href="/raulbenitez/MITO_FIBERS/security">
        <span itemprop="name">Security</span>
            <span class="Counter js-security-deferred-tab-count" hidden></span>
        <meta itemprop="position" content="8">
</a>
      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /raulbenitez/MITO_FIBERS/pulse" href="/raulbenitez/MITO_FIBERS/pulse">
        Pulse
</a>
      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="community /raulbenitez/MITO_FIBERS/community" href="/raulbenitez/MITO_FIBERS/community">
          Community
</a>      </span>

  </nav>
</div>


  </div>

  

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>


<div class="container-lg clearfix new-discussion-timeline  p-responsive">
  <div class="repository-content ">

    
    

  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/raulbenitez/MITO_FIBERS/blob/5007d0e818614a4bd334cee8d1c41c4e5a01b0b2/read_lif.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v22:9e4b9d84b5662752f6f78990924c80c3 -->
    

    <div class="d-flex flex-items-start flex-shrink-0 flex-column flex-md-row pb-3">
      <span class="d-flex flex-justify-between width-full width-md-auto">
        
<details class="details-reset details-overlay branch-select-menu " id="branch-select-menu">
  <summary class="btn css-truncate btn-sm"
           data-hotkey="w"
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target" data-menu-button>master</span>
    <span class="dropdown-caret"></span>
  </summary>

  <details-menu class="SelectMenu SelectMenu--hasFilter" src="/raulbenitez/MITO_FIBERS/refs/master/read_lif.py?source_action=show&amp;source_controller=blob" preload>
    <div class="SelectMenu-modal">
      <include-fragment class="SelectMenu-loading" aria-label="Menu is loading">
        <svg class="octicon octicon-octoface anim-pulse" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"></path></svg>
      </include-fragment>
    </div>
  </details-menu>
</details>

        <div class="BtnGroup flex-shrink-0 d-md-none">
          <a href="/raulbenitez/MITO_FIBERS/find/master"
                class="js-pjax-capture-input btn btn-sm BtnGroup-item"
                data-pjax
                data-hotkey="t">
            Find file
          </a>
          <clipboard-copy value="read_lif.py" class="btn btn-sm BtnGroup-item">
            Copy path
          </clipboard-copy>
        </div>
      </span>
      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal flex-md-self-center ml-md-2 mr-md-3 my-2 my-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="true" href="/raulbenitez/MITO_FIBERS"><span>MITO_FIBERS</span></a></span></span><span class="separator">/</span><strong class="final-path">read_lif.py</strong>
          <span class="separator">/</span><details class="details-reset details-overlay d-inline" id="jumpto-symbol-select-menu">
  <summary class="btn-link link-gray css-truncate" aria-haspopup="true" data-hotkey="r" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_blob_definitions&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_blob_definitions&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="3d51756204e619de494db887431a57bf0b48aa87c7699c2f47df8fad72586483">
      <svg class="octicon octicon-code" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.71967 3.21967C5.01256 2.92678 5.48744 2.92678 5.78033 3.21967C6.07322 3.51256 6.07322 3.98744 5.78033 4.28033L2.06066 8L5.78033 11.7197C6.07322 12.0126 6.07322 12.4874 5.78033 12.7803C5.48744 13.0732 5.01256 13.0732 4.71967 12.7803L0.46967 8.53033C0.176777 8.23744 0.176777 7.76256 0.46967 7.46967L4.71967 3.21967ZM11.2803 3.21967C10.9874 2.92678 10.5126 2.92678 10.2197 3.21967C9.92678 3.51256 9.92678 3.98744 10.2197 4.28033L13.9393 8L10.2197 11.7197C9.92678 12.0126 9.92678 12.4874 10.2197 12.7803C10.5126 13.0732 10.9874 13.0732 11.2803 12.7803L15.5303 8.53033C15.8232 8.23744 15.8232 7.76256 15.5303 7.46967L11.2803 3.21967Z"></path></svg>
    <span data-menu-button>Jump to</span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="SelectMenu SelectMenu--hasFilter" role="menu">
    <div class="SelectMenu-modal">
      <header class="SelectMenu-header">
        <span class="SelectMenu-title">Code definitions</span>
        <button class="SelectMenu-closeButton" type="button" data-toggle-for="jumpto-symbol-select-menu">
          <svg aria-label="Close menu" class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" role="img"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.72 3.72C3.86062 3.57955 4.05125 3.50066 4.25 3.50066C4.44875 3.50066 4.63937 3.57955 4.78 3.72L8 6.94L11.22 3.72C11.2887 3.64631 11.3715 3.58721 11.4635 3.54622C11.5555 3.50523 11.6548 3.48319 11.7555 3.48141C11.8562 3.47963 11.9562 3.49816 12.0496 3.53588C12.143 3.5736 12.2278 3.62974 12.299 3.70096C12.3703 3.77218 12.4264 3.85702 12.4641 3.9504C12.5018 4.04379 12.5204 4.14382 12.5186 4.24452C12.5168 4.34523 12.4948 4.44454 12.4538 4.53654C12.4128 4.62854 12.3537 4.71134 12.28 4.78L9.06 8L12.28 11.22C12.3537 11.2887 12.4128 11.3715 12.4538 11.4635C12.4948 11.5555 12.5168 11.6548 12.5186 11.7555C12.5204 11.8562 12.5018 11.9562 12.4641 12.0496C12.4264 12.143 12.3703 12.2278 12.299 12.299C12.2278 12.3703 12.143 12.4264 12.0496 12.4641C11.9562 12.5018 11.8562 12.5204 11.7555 12.5186C11.6548 12.5168 11.5555 12.4948 11.4635 12.4538C11.3715 12.4128 11.2887 12.3537 11.22 12.28L8 9.06L4.78 12.28C4.63782 12.4125 4.44977 12.4846 4.25547 12.4812C4.06117 12.4777 3.87579 12.399 3.73837 12.2616C3.60096 12.1242 3.52225 11.9388 3.51882 11.7445C3.51539 11.5502 3.58752 11.3622 3.72 11.22L6.94 8L3.72 4.78C3.57955 4.63938 3.50066 4.44875 3.50066 4.25C3.50066 4.05125 3.57955 3.86063 3.72 3.72Z"></path></svg>
        </button>
      </header>
        <div class="SelectMenu-filter">
          <input
            class="SelectMenu-input form-control js-filterable-field"
            id="jumpto-symbols-filter-field"
            type="text"
            autocomplete="off"
            spellcheck="false"
            autofocus
            placeholder="Filter definitions"
            aria-label="Filter definitions">
        </div>
      <div class="SelectMenu-list">
        <div data-filterable-for="jumpto-symbols-filter-field" data-filterable-type="substring">
            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L78">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>Header</span>
              <span class="flex-auto d-flex flex-justify-end">Class</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L87">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>__init__</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L95">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>parse</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L147">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getVersion</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L156">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getName</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L166">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getSeriesHeaders</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L189">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>chooseSerieIndex</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L225">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>chooseSerieHeader</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L236">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>__iter__</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L240">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>SerieHeader</span>
              <span class="flex-auto d-flex flex-justify-end">Class</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L251">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>__init__</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L254">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getName</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L263">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>isPreview</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L272">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getChannels</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L288">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getDimensions</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L304">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>hasZ</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L315">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getMemorySize</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L329">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getResolution</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L344">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getScannerSetting</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L363">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getFilterSetting</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L383">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getNumberOfElements</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L397">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getVoxelSize</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L408">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getZXratio</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L441">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getTotalDuration</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L455">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getTimeLapse</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L469">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getTimeStamps</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L496">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getRelativeTimeStamps</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L514">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getBytesInc</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L535">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>chooseChannel</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L559">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getNbFrames</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L573">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getBoxShape</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L590">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getFrameShape</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L598">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>get2DShape</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L606">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getNbPixelsPerFrame</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L617">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getNbPixelsPerSlice</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L629">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>get_xml</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L647">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>Reader</span>
              <span class="flex-auto d-flex flex-justify-end">Class</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L658">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>__init__</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L702">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>__readMemoryBlockHeader</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L714">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getSeries</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L727">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>chooseSerie</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L735">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>__iter__</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L739">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>Serie</span>
              <span class="flex-auto d-flex flex-justify-end">Class</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L746">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>__init__</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L751">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getOffset</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L764">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getChannelOffset</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L775">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>get2DSlice</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L798">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>get2DString</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L813">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getFrame</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L839">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getFrame2D</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L860">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getMetadata</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L924">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>saveXML</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L930">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>getVTK</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L949">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>enumByFrame</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}" data-hydro-click-hmac="71d101624b6ccd67555b99fdae0048398cbfcba59154454bbe63161ab639266d" href="/raulbenitez/MITO_FIBERS/blob/master/read_lif.py#L959">
              <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M13.78 4.22C13.9204 4.36062 13.9993 4.55125 13.9993 4.75C13.9993 4.94875 13.9204 5.13937 13.78 5.28L6.53 12.53C6.38937 12.6704 6.19875 12.7493 6 12.7493C5.80125 12.7493 5.61062 12.6704 5.47 12.53L2.22 9.28C2.08752 9.13782 2.0154 8.94978 2.01882 8.75547C2.02225 8.56117 2.10096 8.37579 2.23838 8.23837C2.37579 8.10096 2.56118 8.02225 2.75548 8.01882C2.94978 8.01539 3.13782 8.08752 3.28 8.22L6 10.94L12.72 4.22C12.8606 4.07955 13.0512 4.00066 13.25 4.00066C13.4487 4.00066 13.6394 4.07955 13.78 4.22Z"></path></svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text>enumBySlice</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>        </div>
      </div>
      <footer class="SelectMenu-footer">
        <div class="d-flex flex-justify-between">
          Code navigation index up-to-date
          <svg class="octicon octicon-dot-fill text-green" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 13C10.7614 13 13 10.7614 13 8C13 5.23858 10.7614 3 8 3C5.23858 3 3 5.23858 3 8C3 10.7614 5.23858 13 8 13Z"></path></svg>
        </div>
      </footer>
    </div>
  </details-menu>
</details>

      </h2>

      <div class="BtnGroup flex-shrink-0 d-none d-md-inline-block">
        <a href="/raulbenitez/MITO_FIBERS/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy value="read_lif.py" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>



    <include-fragment src="/raulbenitez/MITO_FIBERS/contributors/master/read_lif.py" class="Box Box--condensed commit-loader">
      <div class="Box-body bg-blue-light f6">
        Fetching contributors&hellip;
      </div>

      <div class="Box-body d-flex flex-items-center" >
        <img alt="" class="loader-loading mr-2" src="https://github.githubassets.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" height="16" />
        <span class="text-red h6 loader-error">Cannot retrieve contributors at this time</span>
      </div>
</include-fragment>





    <div class="Box mt-3 position-relative
      ">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">
  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">

      968 lines (815 sloc)
      <span class="file-info-divider"></span>
    38.4 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/raulbenitez/MITO_FIBERS/raw/master/read_lif.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/raulbenitez/MITO_FIBERS/blame/master/read_lif.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/raulbenitez/MITO_FIBERS/commits/master/read_lif.py">History</a>
    </div>


    <div>
          <a class="btn-octicon tooltipped tooltipped-nw js-remove-unless-platform"
             data-platforms="windows,mac"
             href="x-github-client://openRepo/https://github.com/raulbenitez/MITO_FIBERS?branch=master&amp;filepath=read_lif.py"
             aria-label="Open this file in GitHub Desktop"
             data-ga-click="Repository, open with desktop">
              <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.75 2.5H14.25C14.3881 2.5 14.5 2.61193 14.5 2.75V10.25C14.5 10.3881 14.3881 10.5 14.25 10.5H1.75C1.61193 10.5 1.5 10.3881 1.5 10.25V2.75C1.5 2.61193 1.61193 2.5 1.75 2.5ZM14.25 1H1.75C0.783502 1 0 1.7835 0 2.75V10.25C0 11.2165 0.783502 12 1.75 12H5.47703C5.37794 13.041 4.95684 13.8724 4.18494 14.7568C3.99156 14.9784 3.94553 15.2926 4.06724 15.5604C4.18894 15.8281 4.4559 16 4.75001 16H11.25C11.5441 16 11.8111 15.8281 11.9328 15.5604C12.0545 15.2926 12.0085 14.9784 11.8151 14.7568C11.0432 13.8724 10.6221 13.041 10.523 12H14.25C15.2165 12 16 11.2165 16 10.25V2.75C16 1.7835 15.2165 1 14.25 1ZM9.01784 12H6.98218C6.91392 12.9377 6.651 13.7473 6.21733 14.5H9.78269C9.34903 13.7473 9.08611 12.9377 9.01784 12Z"></path></svg>
          </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/raulbenitez/MITO_FIBERS/edit/master/read_lif.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="ErpRB6miKaZirOgBXgtkC8joKBpc7EiAY9VhALqdFal/wtl1/ocbyHVV+G9oPEwR3ZpaY98LHwak9ZB2X/stwg==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Edit this file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.0126 1.42678C11.696 0.74336 12.804 0.743362 13.4874 1.42678L14.5732 2.51257C15.2566 3.19598 15.2566 4.30402 14.5732 4.98744L5.96355 13.5971C5.75325 13.8074 5.49283 13.9606 5.20687 14.0423L1.95603 14.9711C1.69413 15.046 1.41226 14.9729 1.21966 14.7803C1.02706 14.5877 0.954017 14.3059 1.02884 14.044L1.95766 10.7931C2.03936 10.5072 2.19259 10.2467 2.40289 10.0364L11.0126 1.42678ZM12.4268 2.48744C12.3291 2.38981 12.1708 2.38981 12.0732 2.48744L10.8106 3.75L12.25 5.18934L13.5126 3.92678C13.6102 3.82915 13.6102 3.67086 13.5126 3.57323L12.4268 2.48744ZM11.1893 6.25L9.74999 4.81066L3.46355 11.0971C3.43351 11.1271 3.41162 11.1643 3.39994 11.2052L2.842 13.158L4.79479 12.6C4.83564 12.5884 4.87284 12.5665 4.90289 12.5364L11.1893 6.25Z"></path></svg>
            </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/raulbenitez/MITO_FIBERS/delete/master/read_lif.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="mdiOZ8JW89eWOkM+bpOqyOteoRZzM/uqiRhyynlG1LYsqKTWgh73IOmDisTKRcn4AqR/fX046KmdPqXMlGhslA==" />
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
              aria-label="Delete this file" data-disable-with>
              <svg class="octicon octicon-trashcan" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M6.5 1.75C6.5 1.61193 6.61193 1.5 6.75 1.5H9.25C9.38807 1.5 9.5 1.61193 9.5 1.75V3H6.5V1.75ZM11 1.75V3H13.25C13.6642 3 14 3.33579 14 3.75C14 4.16421 13.6642 4.5 13.25 4.5H2.75C2.33579 4.5 2 4.16421 2 3.75C2 3.33579 2.33579 3 2.75 3H5V1.75C5 0.783502 5.7835 0 6.75 0H9.25C10.2165 0 11 0.783502 11 1.75ZM4.49627 6.67537C4.45506 6.26321 4.08753 5.9625 3.67537 6.00372C3.26321 6.04493 2.9625 6.41247 3.00372 6.82462L3.66367 13.4241C3.75313 14.3187 4.50592 15 5.40498 15H10.595C11.4941 15 12.2469 14.3187 12.3363 13.4241L12.9963 6.82462C13.0375 6.41247 12.7368 6.04493 12.3246 6.00372C11.9125 5.9625 11.5449 6.26321 11.5037 6.67537L10.8438 13.2749C10.831 13.4027 10.7234 13.5 10.595 13.5H5.40498C5.27655 13.5 5.169 13.4027 5.15622 13.2749L4.49627 6.67537Z"></path></svg>
            </button>
</form>    </div>
  </div>
</div>


        <div class="js-notice border-bottom p-2">
          <div class="d-flex rounded-1 code-navigation-banner">
            <div class="col-6 pt-4 pl-4 pb-4">
              <div class="d-flex flex-items-center f6">
                <h3 class="mr-2">Code navigation is available!</h3>
              </div>
              <p class="text-gray pt-2">
                Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository.
                <a href="https://help.github.com/en/articles/navigating-code-on-github">Learn more</a>
              </p>
            </div>
            <div class="col-6 p-2 text-right code-navigation-banner-illo">
              <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-notice-dismiss" action="/settings/dismiss-notice/aleph_code_navigation_banner" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="7Ncaxc6KMOTTf6SXcgkvDCVHMlFYXSN3zPNcaa0vALCTm+OVvHDRMo5M7RyKrOon6eTEF0VRYxYdr73FdSMuKQ==" />
                <button name="button" type="submit" class="btn-link link-gray" aria-label="Dismiss">
                  <svg width="20" height="20" class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.72 3.72C3.86062 3.57955 4.05125 3.50066 4.25 3.50066C4.44875 3.50066 4.63937 3.57955 4.78 3.72L8 6.94L11.22 3.72C11.2887 3.64631 11.3715 3.58721 11.4635 3.54622C11.5555 3.50523 11.6548 3.48319 11.7555 3.48141C11.8562 3.47963 11.9562 3.49816 12.0496 3.53588C12.143 3.5736 12.2278 3.62974 12.299 3.70096C12.3703 3.77218 12.4264 3.85702 12.4641 3.9504C12.5018 4.04379 12.5204 4.14382 12.5186 4.24452C12.5168 4.34523 12.4948 4.44454 12.4538 4.53654C12.4128 4.62854 12.3537 4.71134 12.28 4.78L9.06 8L12.28 11.22C12.3537 11.2887 12.4128 11.3715 12.4538 11.4635C12.4948 11.5555 12.5168 11.6548 12.5186 11.7555C12.5204 11.8562 12.5018 11.9562 12.4641 12.0496C12.4264 12.143 12.3703 12.2278 12.299 12.299C12.2278 12.3703 12.143 12.4264 12.0496 12.4641C11.9562 12.5018 11.8562 12.5204 11.7555 12.5186C11.6548 12.5168 11.5555 12.4948 11.4635 12.4538C11.3715 12.4128 11.2887 12.3537 11.22 12.28L8 9.06L4.78 12.28C4.63782 12.4125 4.44977 12.4846 4.25547 12.4812C4.06117 12.4777 3.87579 12.399 3.73837 12.2616C3.60096 12.1242 3.52225 11.9388 3.51882 11.7445C3.51539 11.5502 3.58752 11.3622 3.72 11.22L6.94 8L3.72 4.78C3.57955 4.63938 3.50066 4.44875 3.50066 4.25C3.50066 4.05125 3.57955 3.86063 3.72 3.72Z"></path></svg>
</button></form>            </div>
          </div>
        </div>

      

  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8" data-paste-markdown-skip>
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class=pl-c># -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#  The code was origionally done by Mathieu Leocmach</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#  It was part of the Colloids library (https://github.com/MathieuLeocmach/colloids)</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#  It is modified by Yushi Yang (yushi.yang@bristol.ac.uk) to be more compatable</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#  with different python version and confocal machines</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#  Since its&#39; original version use GPL License, it&#39;s restricted GPL as well</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    Modification June 2019 by M. Leocmach /C. Ybert:</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        0- Note about good practices: semi-private attributes should only be accessed from a method getXXX(). Semi-privacy is chosen here to emphasize </span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#           that values are not supposed to be changed (they correspond to the *fixed* experimental conditions)</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        1- Limit read_lif to its main purpose (remove analysis functions getNeighbourhood() and getRadius, and associated library import)</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        2- Add a getFilterSetting method to SerieHeader Class</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        3- Modify Header.parse method (remove initial storage of all timestamps)</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        5- Expand (a bit) the function description</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        6- Move all double underscore attributes to simple underscore (semi-private ones) and corrected uneffective hasattr() tests</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        7- Remove get2DImage() methods</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        8- Add a getFrame2D() method to extract a 2D image. As for getFrame() it lacks proper conditional testing to accomodate (or report error)</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#           depending on the type of data (XYT, XYZT, ...). It is based on the inner loop in getFrame so that it might be possible to</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#           rewrite getFrame() using getFrame2D().</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        BUGS: - getMetadata() doesn&#39;t support XY frames (no z)</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#              - getFrame() doesn&#39;t support XY frames (no z)</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#              - get2DStrings() doesn&#39;t support XY frames (no z)</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#              - enumByFrame() and enumBySlice() lacks some conditional testing against the data frame type</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#        ToDo: - Correct Bugs</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#              - Convert TimeStamps into seconds</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#              - getZXratio it would be more consistent to use getDimensions() to obtain the information</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#              - Automatic type conversion of SeriesHeader data (in ScannerSetting and FilterSetting) using the VariantType data from VisualBasic</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#                {0: Empty, 1: Null, 2: Short, 3: integer, 4: single, 5: double, 6: currency, 7: date, 8: string, 9: object, 10: error</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#                 11: boolean, 12: variant, 13: dataObject, 14: decimal, 17: byte, 18: char, 20: long, 36: UserDefined, 8192: array}</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class=pl-c># ============== origional information ====================</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    Copyright 2009 Mathieu Leocmach</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    This file is part of Colloids.</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    Colloids is free software: you can redistribute it and/or modify</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    it under the terms of the GNU General Public License as published by</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    the Free Software Foundation, either version 3 of the License, or</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    (at your option) any later version.</span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    Colloids is distributed in the hope that it will be useful,</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    GNU General Public License for more details.</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    You should have received a copy of the GNU General Public License</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#    along with Colloids.  If not, see &lt;http://www.gnu.org/licenses/&gt;.</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>struct</span>, <span class=pl-s1>io</span>, <span class=pl-s1>re</span>, <span class=pl-s1>sys</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>xml</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>xml</span>.<span class=pl-s1>dom</span>.<span class=pl-s1>minidom</span> <span class=pl-k>import</span> <span class=pl-s1>parse</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>numpy</span> <span class=pl-k>as</span> <span class=pl-s1>np</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>warnings</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>dimName</span> <span class=pl-c1>=</span> {<span class=pl-c1>1</span>: <span class=pl-s>&quot;X&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">           <span class=pl-c1>2</span>: <span class=pl-s>&quot;Y&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">           <span class=pl-c1>3</span>: <span class=pl-s>&quot;Z&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">           <span class=pl-c1>4</span>: <span class=pl-s>&quot;T&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">           <span class=pl-c1>5</span>: <span class=pl-s>&quot;Lambda&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">           <span class=pl-c1>6</span>: <span class=pl-s>&quot;Rotation&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">           <span class=pl-c1>7</span>: <span class=pl-s>&quot;XT Slices&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">           <span class=pl-c1>8</span>: <span class=pl-s>&quot;TSlices&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">           <span class=pl-c1>10</span>: <span class=pl-s>&quot;unknown&quot;</span>}</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>channelTag</span> <span class=pl-c1>=</span> [<span class=pl-s>&quot;Gray&quot;</span>, <span class=pl-s>&quot;Red&quot;</span>, <span class=pl-s>&quot;Green&quot;</span>, <span class=pl-s>&quot;Blue&quot;</span>]</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>Header</span>:</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">    <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    The XML header of a Leica LIF files</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    </span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Attributes:: are all semi-private (should only be accessed from a method getXXX()) </span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                 as values are not supposed to be changed (they correspond to the *fixed* experimental conditions)</span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                 _version, _name, _seriesHeaders, </span></td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>xmlHeaderFileName</span>, <span class=pl-s1>quick</span><span class=pl-c1>=</span><span class=pl-c1>True</span>):</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>sys</span>.<span class=pl-s1>version_info</span> <span class=pl-c1>&gt;</span> (<span class=pl-c1>3</span>, <span class=pl-c1>0</span>):</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>with</span> <span class=pl-en>open</span>(<span class=pl-s1>xmlHeaderFileName</span>, <span class=pl-s1>encoding</span><span class=pl-c1>=</span><span class=pl-s>&quot;latin-1&quot;</span>) <span class=pl-k>as</span> <span class=pl-s1>f</span>:</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-en>parse</span>(<span class=pl-s1>f</span>, <span class=pl-s1>quick</span>)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>with</span> <span class=pl-en>open</span>(<span class=pl-s1>xmlHeaderFileName</span>) <span class=pl-k>as</span> <span class=pl-s1>f</span>:</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-en>parse</span>(<span class=pl-s1>f</span>, <span class=pl-s1>quick</span>)</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>parse</span>(<span class=pl-s1>self</span>, <span class=pl-s1>xmlHeaderFile</span>, <span class=pl-s1>quick</span><span class=pl-c1>=</span><span class=pl-c1>True</span>):</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Parse the usefull part of the xml header. Non ascii characters are stripped</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Args:</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            </span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            quick (Boolean). If True Time Stamps are also stripped from the xmlHeader</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            </span></td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        .. warnings:: `quick == True` forbids future access to TimeStamps unless re-opening of original .lif file</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># to strip the non ascii characters</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>t</span> <span class=pl-c1>=</span> <span class=pl-s>&quot;&quot;</span>.<span class=pl-en>join</span>(<span class=pl-en>map</span>(<span class=pl-s1>chr</span>, <span class=pl-en>list</span>(<span class=pl-en>range</span>(<span class=pl-c1>256</span>))))</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>d</span> <span class=pl-c1>=</span> <span class=pl-s>&quot;&quot;</span>.<span class=pl-en>join</span>(<span class=pl-en>map</span>(<span class=pl-s1>chr</span>, <span class=pl-en>list</span>(<span class=pl-en>range</span>(<span class=pl-c1>128</span>, <span class=pl-c1>256</span>))))</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>sys</span>.<span class=pl-s1>version_info</span> <span class=pl-c1>&gt;</span> (<span class=pl-c1>3</span>, <span class=pl-c1>0</span>):</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>trans</span> <span class=pl-c1>=</span> <span class=pl-s1>str</span>.<span class=pl-en>maketrans</span>(<span class=pl-s>&#39;&#39;</span>, <span class=pl-s>&#39;&#39;</span>, <span class=pl-s1>d</span>)</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>lightXML</span> <span class=pl-c1>=</span> <span class=pl-s1>io</span>.<span class=pl-v>StringIO</span>()</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>import</span> <span class=pl-v>StringIO</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>trans</span> <span class=pl-c1>=</span> {<span class=pl-en>ord</span>(<span class=pl-s1>c</span>): <span class=pl-c1>None</span> <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-s1>d</span>}</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>lightXML</span> <span class=pl-c1>=</span> <span class=pl-v>StringIO</span>.<span class=pl-v>StringIO</span>()</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>quick</span>:</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>xmlHeaderFile</span>.<span class=pl-en>seek</span>(<span class=pl-c1>0</span>)</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>sys</span>.<span class=pl-s1>version_info</span> <span class=pl-c1>&gt;</span> (<span class=pl-c1>3</span>, <span class=pl-c1>0</span>):</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>line</span> <span class=pl-c1>in</span> <span class=pl-s1>xmlHeaderFile</span>:</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>lightXML</span>.<span class=pl-en>write</span>(<span class=pl-s1>line</span>.<span class=pl-en>translate</span>(<span class=pl-s1>trans</span>))</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>line</span> <span class=pl-c1>in</span> <span class=pl-s1>xmlHeaderFile</span>:</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>try</span>:</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">                        <span class=pl-s1>lightXML</span>.<span class=pl-en>write</span>(<span class=pl-s1>line</span>.<span class=pl-en>translate</span>(<span class=pl-s1>t</span>, <span class=pl-s1>d</span>))</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>except</span> <span class=pl-v>TypeError</span>:</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">                        <span class=pl-s1>lightXML</span>.<span class=pl-en>write</span>(<span class=pl-s1>line</span>.<span class=pl-en>translate</span>(<span class=pl-s1>trans</span>))</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># to strip the time stamps</span></td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>m</span> <span class=pl-c1>=</span> <span class=pl-s1>re</span>.<span class=pl-en>compile</span>(</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>r&#39;&#39;&#39;&lt;TimeStamp HighInteger=&quot;[0-9]*&quot; LowInteger=&quot;[0-9]*&quot;/&gt;|&#39;&#39;&#39;</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">                <span class=pl-c1>+</span> <span class=pl-s>r&#39;&#39;&#39;&lt;RelTimeStamp Time=&quot;[0-9.]*&quot; Frame=&quot;[0-9]*&quot;/&gt;|&#39;&#39;&#39;</span></td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">                <span class=pl-c1>+</span> <span class=pl-s>r&#39;&#39;&#39;&lt;RelTimeStamp Frame=&quot;[0-9]*&quot; Time=&quot;[0-9.]*&quot;/&gt;&#39;&#39;&#39;</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>sys</span>.<span class=pl-s1>version_info</span> <span class=pl-c1>&gt;</span> (<span class=pl-c1>3</span>, <span class=pl-c1>0</span>):</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>line</span> <span class=pl-c1>in</span> <span class=pl-s1>xmlHeaderFile</span>:</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>lightXML</span>.<span class=pl-en>write</span>(<span class=pl-s>&#39;&#39;</span>.<span class=pl-en>join</span>(<span class=pl-s1>m</span>.<span class=pl-en>split</span>(<span class=pl-s1>line</span>)).<span class=pl-en>translate</span>(<span class=pl-s1>trans</span>))</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>line</span> <span class=pl-c1>in</span> <span class=pl-s1>xmlHeaderFile</span>:</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>try</span>:</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">                        <span class=pl-s1>lightXML</span>.<span class=pl-en>write</span>(<span class=pl-s>&#39;&#39;</span>.<span class=pl-en>join</span>(<span class=pl-s1>m</span>.<span class=pl-en>split</span>(<span class=pl-s1>line</span>)).<span class=pl-en>translate</span>(<span class=pl-s1>t</span>, <span class=pl-s1>d</span>))</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>except</span> <span class=pl-v>TypeError</span>:</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">                        <span class=pl-s1>lightXML</span>.<span class=pl-en>write</span>(<span class=pl-s>&#39;&#39;</span>.<span class=pl-en>join</span>(<span class=pl-s1>m</span>.<span class=pl-en>split</span>(<span class=pl-s1>line</span>)).<span class=pl-en>translate</span>(<span class=pl-s1>trans</span>))</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>lightXML</span>.<span class=pl-en>seek</span>(<span class=pl-c1>0</span>)</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>xmlHeader</span> <span class=pl-c1>=</span> <span class=pl-en>parse</span>(<span class=pl-s1>lightXML</span>)</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getVersion</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the version of the Data Container Header</span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_version`</span></td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_version&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_version</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>xmlHeader</span>.<span class=pl-s1>documentElement</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Version&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>int</span>(<span class=pl-s1>self</span>.<span class=pl-s1>_version</span>)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getName</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the name of current lif file (without extension .lif)</span></td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_name`</span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_name&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_name</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>xmlHeader</span>.<span class=pl-s1>documentElement</span>. \</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">                <span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&#39;Element&#39;</span>)[<span class=pl-c1>0</span>].<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Name&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_name</span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getSeriesHeaders</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the Series Headers of all series contained in the .lif file</span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_seriesHeaders`</span></td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_seriesHeaders&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>root</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>xmlHeader</span>.<span class=pl-s1>documentElement</span></td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>headers</span> <span class=pl-c1>=</span> []</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>counter</span> <span class=pl-c1>=</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>element</span> <span class=pl-c1>in</span> <span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&#39;Element&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>element_nodes</span> <span class=pl-c1>=</span> [<span class=pl-s1>node</span> <span class=pl-k>for</span> <span class=pl-s1>node</span> <span class=pl-c1>in</span> <span class=pl-s1>element</span>.<span class=pl-s1>childNodes</span> <span class=pl-k>if</span> <span class=pl-s1>node</span>.<span class=pl-v>ELEMENT_NODE</span> <span class=pl-c1>==</span> <span class=pl-c1>1</span>]</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>memory_nodes</span> <span class=pl-c1>=</span> [<span class=pl-s1>node</span> <span class=pl-k>for</span> <span class=pl-s1>node</span> <span class=pl-c1>in</span> <span class=pl-s1>element_nodes</span> <span class=pl-k>if</span> (<span class=pl-s1>node</span>.<span class=pl-s1>localName</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;Memory&#39;</span>)]</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-en>len</span>(<span class=pl-s1>memory_nodes</span>) <span class=pl-c1>&gt;</span> <span class=pl-c1>0</span>:</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>counter</span> <span class=pl-c1>+=</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>memory_nodes</span> <span class=pl-c1>=</span> <span class=pl-s1>memory_nodes</span>[<span class=pl-c1>0</span>]</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>size</span> <span class=pl-c1>=</span> <span class=pl-s1>memory_nodes</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Size&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>if</span> <span class=pl-s1>size</span>:</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>if</span> <span class=pl-en>int</span>(<span class=pl-s1>size</span>) <span class=pl-c1>&gt;</span> <span class=pl-c1>0</span>:</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">                            <span class=pl-s1>headers</span>.<span class=pl-en>append</span>(<span class=pl-v>SerieHeader</span>(<span class=pl-s1>element</span>))</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_seriesHeaders</span> <span class=pl-c1>=</span> <span class=pl-s1>headers</span></td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_seriesHeaders</span></td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>chooseSerieIndex</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Interactive selection of the desired serie.</span></td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Print a list of all Series specifying: index, Name, Channel number and Tag, and stack dimensions X, Y, Z, T,...</span></td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Promt for selecting a Serie number.</span></td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>st</span> <span class=pl-c1>=</span> <span class=pl-s>&quot;Experiment: %s<span class=pl-cce>\n</span>&quot;</span> <span class=pl-c1>%</span> <span class=pl-s1>self</span>.<span class=pl-en>getName</span>()</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>i</span>, <span class=pl-s1>s</span> <span class=pl-c1>in</span> <span class=pl-en>enumerate</span>(<span class=pl-s1>self</span>.<span class=pl-en>getSeriesHeaders</span>()):</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># s = Serie(serie)</span></td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>st</span> <span class=pl-c1>+=</span> <span class=pl-s>&quot;(%i) %s: %i channels and %i dimensions<span class=pl-cce>\n</span>&quot;</span> <span class=pl-c1>%</span> (</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>i</span>, <span class=pl-s1>s</span>.<span class=pl-en>getName</span>(), <span class=pl-en>len</span>(<span class=pl-s1>s</span>.<span class=pl-en>getChannels</span>()), <span class=pl-en>len</span>(<span class=pl-s1>s</span>.<span class=pl-en>getDimensions</span>())</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-s1>s</span>.<span class=pl-en>getChannels</span>():</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>st</span> <span class=pl-c1>+=</span> <span class=pl-s>&quot; %s&quot;</span> <span class=pl-c1>%</span> <span class=pl-s1>channelTag</span>[<span class=pl-en>int</span>(<span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;ChannelTag&quot;</span>))]</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>s</span>.<span class=pl-en>getDimensions</span>():</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>st</span> <span class=pl-c1>+=</span> <span class=pl-s>&quot; %s%i&quot;</span> <span class=pl-c1>%</span> (</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>dimName</span>[<span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;DimID&quot;</span>))],</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">                    <span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;NumberOfElements&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">                )</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>st</span> <span class=pl-c1>+=</span> <span class=pl-s>&quot;<span class=pl-cce>\n</span>&quot;</span></td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>print</span>(<span class=pl-s1>st</span>)</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-en>len</span>(<span class=pl-s1>self</span>.<span class=pl-en>getSeriesHeaders</span>()) <span class=pl-c1>&lt;</span> <span class=pl-c1>2</span>:</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>r</span> <span class=pl-c1>=</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>while</span> (<span class=pl-c1>True</span>):</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>try</span>:</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>r</span> <span class=pl-c1>=</span> <span class=pl-en>int</span>(<span class=pl-en>input</span>(<span class=pl-s>&quot;Choose a serie --&gt; &quot;</span>))</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>if</span> <span class=pl-s1>r</span> <span class=pl-c1>&lt;</span> <span class=pl-c1>0</span> <span class=pl-c1>or</span> <span class=pl-s1>r</span> <span class=pl-c1>&gt;</span> <span class=pl-en>len</span>(<span class=pl-s1>self</span>.<span class=pl-en>getSeriesHeaders</span>()):</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>()</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>break</span></td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>except</span> <span class=pl-v>ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">                    <span class=pl-en>print</span>(<span class=pl-s>&quot;Oops!  That was no valid number.  Try again...&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>r</span></td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>chooseSerieHeader</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Interactive selection of the desired serie header.</span></td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Print a list of all Series specifying: index, Name, Channel number and Tag, and stack dimensions X, Y, Z, T,...</span></td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Promt for selecting a Serie number.</span></td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-en>getSeriesHeaders</span>()[<span class=pl-s1>self</span>.<span class=pl-en>chooseSerieIndex</span>()]</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__iter__</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>iter</span>(<span class=pl-s1>self</span>.<span class=pl-en>getSeriesHeaders</span>())</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>SerieHeader</span>:</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">    <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    The part of the XML header of a Leica LIF files concerning a given serie</span></td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    </span></td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Attributes:: are all semi-private (should only be accessed from a method getXXX()) </span></td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                 as values are not supposed to be changed (they correspond to the *fixed* experimental conditions)</span></td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                 _name, _isPreview, _channels, _dimensions, _memorySize, _resolution, _numberOfElements, _duration,</span></td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                 _timeStamps, _relTimeStamps, _nbFrames, _boxShape, _nbPixelsPerFrame, _nbPixelsPerSlice, etc.</span></td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    </span></td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>serieElement</span>):</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>root</span> <span class=pl-c1>=</span> <span class=pl-s1>serieElement</span></td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getName</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the Name of the Serie</span></td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_name`</span></td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_name&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_name</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Name&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_name</span></td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>isPreview</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_isPreview&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_isPreview</span> <span class=pl-c1>=</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;Attachment&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Name&quot;</span>) <span class=pl-c1>==</span> <span class=pl-s>&quot;PreviewMarker&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-s1>_isPreview</span> <span class=pl-c1>=</span> <span class=pl-en>bool</span>(<span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;isPreviewImage&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>break</span></td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_isPreview</span></td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getChannels</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Extract the DOM elements describing the used channels.</span></td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_channels`</span></td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: List of DOM elements</span></td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Use: To recover information contained in `chosen_serie.getChannels()`, iterate over the elements and apply `.getAttribute(&#39;Keyword&#39;)` method</span></td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Keywords: Refer to xml file for a list of relevant Keywords. Examples: DataType, ChannelTag, Resolution, NameOfMeasuredQuantity, Min, Max, Unit, </span></td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                  LUTName, IsLUTInverted, BytesInc, BitInc</span></td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_channels&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_channels</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;ChannelDescription&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_channels</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getDimensions</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Extract the DOM elements describing the used channels.</span></td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_dimensions`</span></td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                </span></td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: List of DOM elements</span></td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Use: To recover information contained in `chosen_serie.getDimensionss()`, iterate over the elements and apply `.getAttribute(&#39;Keyword&#39;) method</span></td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Keywords: Refer to xml file for a list of relevant Keywords. Examples: DimID, NumberOfElements, Origin, Length, Unit, BitInc, BytesInc</span></td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_dimensions&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_dimensions</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;DimensionDescription&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_dimensions</span></td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>hasZ</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Check if current serie includes Z stacking</span></td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: Boolean value</span></td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>getDimensions</span>():</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>dimName</span>[<span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;DimID&quot;</span>))] <span class=pl-c1>==</span> <span class=pl-s>&quot;Z&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>return</span> <span class=pl-c1>True</span></td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-c1>False</span></td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getMemorySize</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the Memory size of the current Serie</span></td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_memorySize`</span></td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: Memory size as int</span></td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_memorySize&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>m</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;Memory&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">                <span class=pl-c># to ensure the Memory node is the child of root</span></td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>m</span>.<span class=pl-s1>parentNode</span> <span class=pl-c1>is</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>:</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-s1>_memorySize</span> <span class=pl-c1>=</span> <span class=pl-en>int</span>(<span class=pl-s1>m</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Size&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_memorySize</span></td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getResolution</span>(<span class=pl-s1>self</span>, <span class=pl-s1>channel</span>):</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the BitDepth Resolution of a given Channel using .getChannels() method</span></td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_resolution`</span></td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        arg:: channel number (int)</span></td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: Bit Depth resolution as int</span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_resolution&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_resolution</span> <span class=pl-c1>=</span> <span class=pl-en>int</span>(</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-en>getChannels</span>()[<span class=pl-s1>channel</span>].<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Resolution&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_resolution</span></td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getScannerSetting</span>(<span class=pl-s1>self</span>, <span class=pl-s1>identifier</span>):</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Access to the value of one of the Experimental Condition elements under ScannerSettingRecord TagName</span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_&quot;identifier&quot;`</span></td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        arg:: identifier (string) as the name of the Attribute looked for.</span></td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line"><span class=pl-s>              Refer to xml file for a list of relevant identifier: dblPinhole, dblSizeX, dblSizeY, dblVoxelX, dblVoxelY, dblZoom, </span></td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line"><span class=pl-s>              nAccumulation, nAverageFrame, nAverageLine, nChannels, nDelayTime_ms, nLineAccumulation, nRepeatActions, ...</span></td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        return: The value (&#39;Variant&#39;) of the required Attribute (&#39;identifier&#39;) as a *string* </span></td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span> <span class=pl-s1>identifier</span>):</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;ScannerSettingRecord&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Identifier&quot;</span>) <span class=pl-c1>==</span> <span class=pl-s1>identifier</span>:</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">                    <span class=pl-en>setattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span> <span class=pl-s1>identifier</span>, <span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Variant&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>break</span></td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>getattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span> <span class=pl-s1>identifier</span>)</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getFilterSetting</span>(<span class=pl-s1>self</span>, <span class=pl-s1>objectName</span>):</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Access to the value of one of the Experimental Condition elements under `FilterSettingRecord TagName`</span></td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_&quot;objectName&quot;`</span></td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        arg:: objectName (string) as the name of the Object looked for.</span></td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line"><span class=pl-s>              Refer to xml file for a list of relevant objectName: e.g. &#39;Scan Head&#39; yields information about scanner</span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        return: Unlike identifier in getScannerSetting, a single objectname has multiple occurences, </span></td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                hence getFilterSetting returns a dictionnary of all {Attributes: Variant}, with values &#39;Variant&#39; being strings </span></td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span> <span class=pl-s1>objectName</span>):</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>obj</span> <span class=pl-c1>=</span> <span class=pl-en>dict</span>()</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;FilterSettingRecord&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;ObjectName&quot;</span>) <span class=pl-c1>==</span> <span class=pl-s1>objectName</span>:</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>obj</span>[<span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Attribute&quot;</span>)] <span class=pl-c1>=</span> <span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Variant&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">            <span class=pl-en>setattr</span>(<span class=pl-s1>self</span>,  <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span> <span class=pl-s1>objectName</span>, <span class=pl-s1>obj</span>)</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>getattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span>  <span class=pl-s1>objectName</span>)</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getNumberOfElements</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Use .getDimensions() method to extact the data dimensions along all axis in order X, Y, Z, T, ...</span></td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_numberOfElements`</span></td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Result: List of integers</span></td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_numberOfElements&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_numberOfElements</span> <span class=pl-c1>=</span> [</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">                <span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;NumberOfElements&quot;</span>)) \</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>getDimensions</span>()</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">            ]</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_numberOfElements</span></td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getVoxelSize</span>(<span class=pl-s1>self</span>, <span class=pl-s1>dimension</span>):</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Use getScannerSetting() to return the resolution</span></td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        arg:: dimension is an integer according to the dimName dictionnary {1: X, 2: Y, 3: Z}</span></td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: Voxel size of specified axis (float)</span></td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>float</span>(<span class=pl-s1>self</span>.<span class=pl-en>getScannerSetting</span>(<span class=pl-s>&quot;dblVoxel%s&quot;</span> <span class=pl-c1>%</span> <span class=pl-s1>dimName</span>[<span class=pl-s1>dimension</span>]))</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getZXratio</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Calculate for the current Serie the ratio between Vertical (Z) and Horizontal (X) image resolutions. Looks for the information either in</span></td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                    - &#39;ScannerSettingRecord&#39; (resolution)</span></td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                    - or in &#39;DimensionDescription&#39; (total size / pixel number)</span></td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: Z/X resolution ratio (float). Return 1.0 if the current Serie has no Z-stack.</span></td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line"><span class=pl-s>               </span></td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>setting_records</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&#39;ScannerSettingRecord&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>dimension_descriptions</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&#39;DimensionDescription&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>hasZ</span>():</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>setting_records</span>:</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>return</span> <span class=pl-en>float</span>(<span class=pl-s1>self</span>.<span class=pl-en>getScannerSetting</span>(<span class=pl-s>&quot;dblVoxelZ&quot;</span>)) <span class=pl-c1>/</span> <span class=pl-en>float</span>(<span class=pl-s1>self</span>.<span class=pl-en>getScannerSetting</span>(<span class=pl-s>&quot;dblVoxelX&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>elif</span> <span class=pl-s1>dimension_descriptions</span>:</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>length_x</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">                    [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Length&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span> <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;1&#39;</span>][<span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>length_z</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">                    [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Length&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span> <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;3&#39;</span>][<span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>number_x</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">                    [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;NumberOfElements&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span></td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">                     <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;1&#39;</span>][</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">                        <span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>number_z</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">                    [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;NumberOfElements&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span></td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">                     <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;3&#39;</span>][</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">                        <span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>psx</span> <span class=pl-c1>=</span> <span class=pl-s1>length_x</span> <span class=pl-c1>/</span> <span class=pl-s1>number_x</span></td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>psz</span> <span class=pl-c1>=</span> <span class=pl-s1>length_z</span> <span class=pl-c1>/</span> <span class=pl-s1>number_z</span></td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>return</span> <span class=pl-s1>psz</span> <span class=pl-c1>/</span> <span class=pl-s1>psx</span></td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>return</span> <span class=pl-c1>1.0</span></td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getTotalDuration</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get total duration of the experiment using the .getDimensions() method</span></td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_duration`</span></td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: duration (float) in seconds</span></td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_duration&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_duration</span> <span class=pl-c1>=</span> <span class=pl-c1>0.0</span></td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>getDimensions</span>():</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>dimName</span>[<span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;DimID&quot;</span>))] <span class=pl-c1>==</span> <span class=pl-s>&quot;T&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-s1>_duration</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Length&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_duration</span></td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getTimeLapse</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get an estimate of the average time lapse between two frames in seconds</span></td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: estimated Lag time in seconds (float)</span></td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        warning:: Note that this value is accessible directly via getScannerSetting(&#39;nDelayTime_ms&#39;)</span></td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line"><span class=pl-s>           </span></td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-en>getNbFrames</span>() <span class=pl-c1>==</span> <span class=pl-c1>1</span>:</td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>return</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-en>getTotalDuration</span>() <span class=pl-c1>/</span> (<span class=pl-s1>self</span>.<span class=pl-en>getNbFrames</span>() <span class=pl-c1>-</span> <span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getTimeStamps</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get a numpy array of all image timeStamps in the Serie.</span></td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_timeStamps`</span></td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: Numpy array of integers with timeStamps of all successives images in the Serie</span></td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        warning:: on first call getTimeStamps() suppresses the data from the XML SerieHeader</span></td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_timeStamps&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>tslist</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;TimeStampList&quot;</span>)[<span class=pl-c1>0</span>]</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>tslist</span>.<span class=pl-en>hasAttribute</span>(<span class=pl-s>&quot;NumberOfTimeStamps&quot;</span>) <span class=pl-c1>and</span> <span class=pl-en>int</span>(<span class=pl-s1>tslist</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;NumberOfTimeStamps&quot;</span>)) <span class=pl-c1>&gt;</span> <span class=pl-c1>0</span>:</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">                <span class=pl-c># SP8 way of storing time stamps in the text of the node as 16bits hexadecimal separated by spaces</span></td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>_timeStamps</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>array</span>([</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">                    <span class=pl-en>int</span>(<span class=pl-s1>h</span>, <span class=pl-c1>16</span>)</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>for</span> <span class=pl-s1>h</span> <span class=pl-c1>in</span> <span class=pl-s1>tslist</span>.<span class=pl-s1>firstChild</span>.<span class=pl-s1>nodeValue</span>.<span class=pl-en>split</span>()</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">                ])</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">                <span class=pl-c># SP5 way of storing time stamps as very verbose XML</span></td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>_timeStamps</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>asarray</span>([</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">                    (<span class=pl-en>int</span>(<span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;HighInteger&quot;</span>)) <span class=pl-c1>&lt;&lt;</span> <span class=pl-c1>32</span>) <span class=pl-c1>+</span> <span class=pl-en>int</span>(<span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;LowInteger&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-s1>tslist</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;TimeStamp&quot;</span>)])</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">                <span class=pl-c># remove the data from XML</span></td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-s1>tslist</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;TimeStamp&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>c</span>.<span class=pl-s1>parentNode</span>.<span class=pl-en>removeChild</span>(<span class=pl-s1>c</span>).<span class=pl-en>unlink</span>()</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_timeStamps</span></td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getRelativeTimeStamps</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get a numpy array of all image relativetimeStamps in the Serie.</span></td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_relTimeStamps`</span></td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: Numpy array of integers with relativetimeStamps of all successives images in the Serie</span></td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        warning:: on first call getRelativeTimeStamps() suppresses the data from the XML SerieHeader</span></td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_relTimeStamps&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_relTimeStamps</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>asarray</span>([</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">                <span class=pl-en>float</span>(<span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;Time&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;RelTimeStamp&quot;</span>)])</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># remove the data from XML</span></td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&quot;RelTimeStamp&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>c</span>.<span class=pl-s1>parentNode</span>.<span class=pl-en>removeChild</span>(<span class=pl-s1>c</span>).<span class=pl-en>unlink</span>()</td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_relTimeStamps</span></td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getBytesInc</span>(<span class=pl-s1>self</span>, <span class=pl-s1>dimension</span>):</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the ByteIncrement of a given dimension in the Serie.</span></td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_&quot;dim&quot;`, with &quot;dim&quot; a string = X, Y, Z, T</span></td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        arg:: dimension either as a string or as its key (integer) in dimName = {1: &quot;X&quot;, 2: &quot;Y&quot;, 3: &quot;Z&quot;, 4: &quot;T&quot;, ...}</span></td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: BytesIncr as integer</span></td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># todo: consider channels</span></td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-en>isinstance</span>(<span class=pl-s1>dimension</span>, <span class=pl-s1>int</span>):</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>dim</span> <span class=pl-c1>=</span> <span class=pl-s1>dimName</span>[<span class=pl-s1>dimension</span>]</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>dim</span> <span class=pl-c1>=</span> <span class=pl-s1>dimension</span></td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span> <span class=pl-s1>dim</span>):</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">            <span class=pl-en>setattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span> <span class=pl-s1>dim</span>, <span class=pl-c1>0</span>)</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>getDimensions</span>():</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>dimName</span>[<span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;DimID&quot;</span>))] <span class=pl-c1>==</span> <span class=pl-s1>dim</span>:</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">                    <span class=pl-en>setattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span> <span class=pl-s1>dim</span>, <span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;BytesInc&quot;</span>)))</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>getattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_&#39;</span> <span class=pl-c1>+</span> <span class=pl-s1>dim</span>)</td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>chooseChannel</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Interactive selection of the channel for the current serie.</span></td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Print the Serie name `chosen_serie.getName() and a list of all channels specifying: index, Color</span></td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Promt for selecting a channel index.</span></td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>st</span> <span class=pl-c1>=</span> <span class=pl-s>&quot;Serie: %s<span class=pl-cce>\n</span>&quot;</span> <span class=pl-c1>%</span> <span class=pl-s1>self</span>.<span class=pl-en>getName</span>()</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>i</span>, <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-en>enumerate</span>(<span class=pl-s1>self</span>.<span class=pl-en>getChannels</span>()):</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>st</span> <span class=pl-c1>+=</span> <span class=pl-s>&quot;(%i) %s<span class=pl-cce>\n</span>&quot;</span> <span class=pl-c1>%</span> (<span class=pl-s1>i</span>, <span class=pl-s1>channelTag</span>[<span class=pl-en>int</span>(<span class=pl-s1>c</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;ChannelTag&quot;</span>))])</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>print</span>(<span class=pl-s1>st</span>)</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-en>len</span>(<span class=pl-s1>self</span>.<span class=pl-en>getChannels</span>()) <span class=pl-c1>&lt;</span> <span class=pl-c1>2</span>:</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>r</span> <span class=pl-c1>=</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>while</span> (<span class=pl-c1>True</span>):</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>try</span>:</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>r</span> <span class=pl-c1>=</span> <span class=pl-en>int</span>(<span class=pl-en>input</span>(<span class=pl-s>&quot;Choose a channel --&gt; &quot;</span>))</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>r</span> <span class=pl-c1>&lt;</span> <span class=pl-c1>0</span> <span class=pl-c1>or</span> <span class=pl-s1>r</span> <span class=pl-c1>&gt;</span> <span class=pl-en>len</span>(<span class=pl-s1>self</span>.<span class=pl-en>getChannels</span>()):</td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>()</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>break</span></td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>except</span> <span class=pl-v>ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">                <span class=pl-en>print</span>(<span class=pl-s>&quot;Oops!  That was no valid number.  Try again...&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>r</span></td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getNbFrames</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the number of frames in the Serie (acquisition at successive times)</span></td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute `_nbFrames`</span></td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: number of frames (integer)</span></td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_nbFrames&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_nbFrames</span> <span class=pl-c1>=</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>getDimensions</span>():</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;DimID&quot;</span>) <span class=pl-c1>==</span> <span class=pl-s>&quot;4&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-s1>_nbFrames</span> <span class=pl-c1>=</span> <span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;NumberOfElements&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_nbFrames</span></td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getBoxShape</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the Shape (spatial) of a frame </span></td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute: _boxShape</span></td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: a list integers [length axis 1, length axis 2, ... ] ordered according to axis number (X, Y, Z)</span></td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_boxShape&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>dims</span> <span class=pl-c1>=</span> {</td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line">                <span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>)): <span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;NumberOfElements&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>getDimensions</span>()</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line">            }</td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># ensure dimensions are sorted (unlike dictionnaries...), keep only spatial dimensions</span></td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_boxShape</span> <span class=pl-c1>=</span> [<span class=pl-s1>s</span> <span class=pl-k>for</span> <span class=pl-s1>d</span>, <span class=pl-s1>s</span> <span class=pl-c1>in</span> <span class=pl-en>sorted</span>(<span class=pl-s1>dims</span>.<span class=pl-en>items</span>()) <span class=pl-k>if</span> <span class=pl-s1>d</span> <span class=pl-c1>&lt;</span> <span class=pl-c1>4</span>]</td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_boxShape</span></td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getFrameShape</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the Shape of the frame (nD image) in C order, that is Z,Y,X </span></td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: list of integers of axis length in Z, Y, X order (reverse as in .getBoxShape())</span></td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-en>getBoxShape</span>()[::<span class=pl-c1>-</span><span class=pl-c1>1</span>]</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>get2DShape</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the Shape of an image using the two first spatial dimensions, in C order, e.g. Y,X</span></td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: list of integers of axis length</span></td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-en>getBoxShape</span>()[:<span class=pl-c1>2</span>][::<span class=pl-c1>-</span><span class=pl-c1>1</span>]</td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getNbPixelsPerFrame</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the total number of pixels in a frame of shape .getBoxShape()</span></td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute: _nbPixelsPerFrame</span></td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: total number of pixels (integer) </span></td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_nbPixelsPerFrame&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_nbPixelsPerFrame</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>prod</span>(<span class=pl-s1>self</span>.<span class=pl-en>getBoxShape</span>())</td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_nbPixelsPerFrame</span></td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getNbPixelsPerSlice</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the total number of pixels in a Slice of shape .get2DShape()</span></td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-private attribute: _nbPixelsPerSlice</span></td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: total number of pixels (integer) </span></td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_nbPixelsPerSlice&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_nbPixelsPerSlice</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>prod</span>(<span class=pl-s1>self</span>.<span class=pl-en>get2DShape</span>())</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_nbPixelsPerSlice</span></td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line"><span class=pl-k>def</span> <span class=pl-en>get_xml</span>(<span class=pl-s1>lif_name</span>):</td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line">    <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Function: Extract the XML header from LIF file and save it. Generated .xml file can be opened in a Web Browser</span></td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    </span></td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Use to examine the global architecture and the keywords associated with usefull information, to use with getXXX() methods</span></td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>with</span> <span class=pl-en>open</span>(<span class=pl-s1>lif_name</span>, <span class=pl-s>&quot;rb&quot;</span>) <span class=pl-k>as</span> <span class=pl-s1>f</span>:</td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>memBlock</span>, <span class=pl-s1>trash</span>, <span class=pl-s1>testBlock</span> <span class=pl-c1>=</span> <span class=pl-s1>struct</span>.<span class=pl-en>unpack</span>(<span class=pl-s>&quot;iic&quot;</span>, <span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-c1>9</span>))</td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>memBlock</span> <span class=pl-c1>!=</span> <span class=pl-c1>112</span>:</td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>Exception</span>(<span class=pl-s>&quot;This is not a valid LIF file&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>testBlock</span> <span class=pl-c1>!=</span> <span class=pl-s>b&#39;*&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>Exception</span>(<span class=pl-s>&quot;Invalid block at %l&quot;</span> <span class=pl-c1>%</span> <span class=pl-s1>f</span>.<span class=pl-en>tell</span>())</td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>memorysize</span>, <span class=pl-c1>=</span> <span class=pl-s1>struct</span>.<span class=pl-en>unpack</span>(<span class=pl-s>&quot;I&quot;</span>, <span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-c1>4</span>))</td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># read and parse the header</span></td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>xml</span> <span class=pl-c1>=</span> <span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-c1>2</span> <span class=pl-c1>*</span> <span class=pl-s1>memorysize</span>).<span class=pl-en>decode</span>(<span class=pl-s>&quot;utf-16&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>xml</span></td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>Reader</span>(<span class=pl-v>Header</span>):</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">    <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Reads Leica LIF files</span></td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    </span></td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Methods: getSeries(), chooseSeries(), __init__(), __iter__(), __readMemoryBlockHeader()</span></td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    </span></td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Semi-Private Attribute:: _series</span></td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                 </span></td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>lifFile</span>, <span class=pl-s1>quick</span><span class=pl-c1>=</span><span class=pl-c1>True</span>):</td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># open file and find it&#39;s size</span></td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-en>isinstance</span>(<span class=pl-s1>lifFile</span>, <span class=pl-s1>io</span>.<span class=pl-v>IOBase</span>):</td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>f</span> <span class=pl-c1>=</span> <span class=pl-s1>lifFile</span></td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>f</span> <span class=pl-c1>=</span> <span class=pl-en>open</span>(<span class=pl-s1>lifFile</span>, <span class=pl-s>&quot;rb&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-c1>0</span>, <span class=pl-c1>2</span>)</td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>filesize</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>tell</span>()</td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-c1>0</span>)</td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># read the size of the memory block containing the XML header</span></td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># takes position at the begining of the XML header</span></td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>xmlHeaderLength</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>__readMemoryBlockHeader</span>()</td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># xmlHeaderLength, = struct.unpack(&quot;L&quot;,self.f.read(4))</span></td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Read the XML header as raw buffer. It should avoid encoding problems</span></td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># but who uses japanese characters anyway</span></td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>xmlHeaderString</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-s1>xmlHeaderLength</span> <span class=pl-c1>*</span> <span class=pl-c1>2</span>).<span class=pl-en>decode</span>(<span class=pl-s>&#39;latin-1&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-en>parse</span>(<span class=pl-s1>io</span>.<span class=pl-v>StringIO</span>(<span class=pl-s1>xmlHeaderString</span>[::<span class=pl-c1>2</span>]), <span class=pl-s1>quick</span>)</td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Index the series offsets</span></td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>offsets</span> <span class=pl-c1>=</span> []</td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>while</span> (<span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>tell</span>() <span class=pl-c1>&lt;</span> <span class=pl-s1>filesize</span>):</td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>memorysize</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>__readMemoryBlockHeader</span>()</td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>while</span> (<span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-c1>1</span>) <span class=pl-c1>!=</span> <span class=pl-s>b&quot;*&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>pass</span></td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># size of the memory description</span></td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>memDescrSize</span>, <span class=pl-c1>=</span> <span class=pl-s1>struct</span>.<span class=pl-en>unpack</span>(<span class=pl-s>&quot;I&quot;</span>, <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-c1>4</span>))</td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>memDescrSize</span> <span class=pl-c1>*=</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># skip the description: we are at the begining of the content</span></td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-s1>memDescrSize</span>, <span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># add image offset if memory size &gt;0</span></td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>memorysize</span> <span class=pl-c1>&gt;</span> <span class=pl-c1>0</span>:</td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>offsets</span>.<span class=pl-en>append</span>(<span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>tell</span>())</td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-s1>memorysize</span>, <span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>quick</span>:</td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># convert immediately the time stamps in XML format to lighweight numpy array</span></td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>s</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>:</td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>s</span>.<span class=pl-en>getTimeStamps</span>()</td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>s</span>.<span class=pl-en>getRelativeTimeStamps</span>()</td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># self.offsets = [long(m.getAttribute(&quot;Size&quot;)) for m in self.xmlHEader.getElementsByTagName(&quot;Memory&quot;)]</span></td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__readMemoryBlockHeader</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>memBlock</span>, <span class=pl-s1>trash</span>, <span class=pl-s1>testBlock</span> <span class=pl-c1>=</span> <span class=pl-s1>struct</span>.<span class=pl-en>unpack</span>(<span class=pl-s>&quot;iic&quot;</span>, <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-c1>9</span>))</td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>memBlock</span> <span class=pl-c1>!=</span> <span class=pl-c1>112</span>:</td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>Exception</span>(<span class=pl-s>&quot;This is not a valid LIF file&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>testBlock</span> <span class=pl-c1>!=</span> <span class=pl-s>b&#39;*&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>Exception</span>(<span class=pl-s>&quot;Invalid block at %d&quot;</span> <span class=pl-c1>%</span> <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>tell</span>())</td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;xmlHeader&#39;</span>) <span class=pl-c1>or</span> <span class=pl-s1>self</span>.<span class=pl-en>getVersion</span>() <span class=pl-c1>&lt;</span> <span class=pl-c1>2</span>:</td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>memorysize</span>, <span class=pl-c1>=</span> <span class=pl-s1>struct</span>.<span class=pl-en>unpack</span>(<span class=pl-s>&quot;I&quot;</span>, <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-c1>4</span>))</td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>memorysize</span>, <span class=pl-c1>=</span> <span class=pl-s1>struct</span>.<span class=pl-en>unpack</span>(<span class=pl-s>&quot;Q&quot;</span>, <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-c1>8</span>))</td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>memorysize</span></td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getSeries</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the experimental Series from the raw .lif file</span></td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Semi-Private Attribute: _series</span></td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: a List of class Serie objects</span></td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&#39;_series&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>_series</span> <span class=pl-c1>=</span> [</td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line">                <span class=pl-v>Serie</span>(<span class=pl-s1>s</span>.<span class=pl-s1>root</span>, <span class=pl-s1>self</span>.<span class=pl-s1>f</span>, <span class=pl-s1>self</span>.<span class=pl-s1>offsets</span>[<span class=pl-s1>i</span>]) <span class=pl-k>for</span> <span class=pl-s1>i</span>, <span class=pl-s1>s</span> <span class=pl-c1>in</span> <span class=pl-en>enumerate</span>(<span class=pl-s1>self</span>.<span class=pl-en>getSeriesHeaders</span>())</td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line">            ]</td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>_series</span></td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>chooseSerie</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: use .chooseSerieIndex() inherited Header method to interactively choose a Serie using .getSeries()</span></td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: the selected class Serie object</span></td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-en>getSeries</span>()[<span class=pl-s1>self</span>.<span class=pl-en>chooseSerieIndex</span>()]</td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__iter__</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>iter</span>(<span class=pl-s1>self</span>.<span class=pl-en>getSeries</span>())</td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>Serie</span>(<span class=pl-v>SerieHeader</span>):</td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">    <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    One of the datasets (Serie) in a .lif file</span></td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    </span></td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Methods: </span></td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>serieElement</span>, <span class=pl-s1>f</span>, <span class=pl-s1>offset</span>):</td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>f</span> <span class=pl-c1>=</span> <span class=pl-s1>f</span></td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>__offset</span> <span class=pl-c1>=</span> <span class=pl-s1>offset</span></td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>root</span> <span class=pl-c1>=</span> <span class=pl-s1>serieElement</span></td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getOffset</span>(<span class=pl-s1>self</span>, <span class=pl-c1>**</span><span class=pl-s1>dimensionsIncrements</span>):</td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the Frame Offset</span></td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        kwargs:: Time, Channel or data type. Default to `channel=0, T=0, dtype=np.uint8`</span></td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>of</span> <span class=pl-c1>=</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>d</span>, <span class=pl-s1>b</span> <span class=pl-c1>in</span> <span class=pl-s1>dimensionsIncrements</span>.<span class=pl-en>items</span>():</td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>of</span> <span class=pl-c1>+=</span> <span class=pl-s1>self</span>.<span class=pl-en>getBytesInc</span>(<span class=pl-s1>d</span>) <span class=pl-c1>*</span> <span class=pl-s1>b</span></td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>of</span> <span class=pl-c1>&gt;=</span> <span class=pl-s1>self</span>.<span class=pl-en>getMemorySize</span>():</td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>IndexError</span>(<span class=pl-s>&quot;offset out of bound&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>__offset</span> <span class=pl-c1>+</span> <span class=pl-s1>of</span></td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getChannelOffset</span>(<span class=pl-s1>self</span>, <span class=pl-s1>channel</span>):</td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get the Channel Offset</span></td>
      </tr>
      <tr>
        <td id="L767" class="blob-num js-line-number" data-line-number="767"></td>
        <td id="LC767" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L768" class="blob-num js-line-number" data-line-number="768"></td>
        <td id="LC768" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        arg:: channel (int)</span></td>
      </tr>
      <tr>
        <td id="L769" class="blob-num js-line-number" data-line-number="769"></td>
        <td id="LC769" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L770" class="blob-num js-line-number" data-line-number="770"></td>
        <td id="LC770" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>channels</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>getChannels</span>()</td>
      </tr>
      <tr>
        <td id="L771" class="blob-num js-line-number" data-line-number="771"></td>
        <td id="LC771" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>channel_node</span> <span class=pl-c1>=</span> <span class=pl-s1>channels</span>[<span class=pl-s1>channel</span>]</td>
      </tr>
      <tr>
        <td id="L772" class="blob-num js-line-number" data-line-number="772"></td>
        <td id="LC772" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>of</span> <span class=pl-c1>=</span> <span class=pl-en>int</span>(<span class=pl-s1>channel_node</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;BytesInc&#39;</span>))</td>
      </tr>
      <tr>
        <td id="L773" class="blob-num js-line-number" data-line-number="773"></td>
        <td id="LC773" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>of</span></td>
      </tr>
      <tr>
        <td id="L774" class="blob-num js-line-number" data-line-number="774"></td>
        <td id="LC774" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L775" class="blob-num js-line-number" data-line-number="775"></td>
        <td id="LC775" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>get2DSlice</span>(<span class=pl-s1>self</span>, <span class=pl-c1>**</span><span class=pl-s1>dimensionsIncrements</span>):</td>
      </tr>
      <tr>
        <td id="L776" class="blob-num js-line-number" data-line-number="776"></td>
        <td id="LC776" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L777" class="blob-num js-line-number" data-line-number="777"></td>
        <td id="LC777" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Use the two first dimensions as image dimension (XY, XZ, YZ). Axis are in C order (last index is X).</span></td>
      </tr>
      <tr>
        <td id="L778" class="blob-num js-line-number" data-line-number="778"></td>
        <td id="LC778" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L779" class="blob-num js-line-number" data-line-number="779"></td>
        <td id="LC779" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: Image as numpy array with the axis in ZY, ZX, or YX order</span></td>
      </tr>
      <tr>
        <td id="L780" class="blob-num js-line-number" data-line-number="780"></td>
        <td id="LC780" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L781" class="blob-num js-line-number" data-line-number="781"></td>
        <td id="LC781" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        warning:: See dtype argument; might not support 16bits encoding</span></td>
      </tr>
      <tr>
        <td id="L782" class="blob-num js-line-number" data-line-number="782"></td>
        <td id="LC782" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L783" class="blob-num js-line-number" data-line-number="783"></td>
        <td id="LC783" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>getDimensions</span>()[:<span class=pl-c1>2</span>]:</td>
      </tr>
      <tr>
        <td id="L784" class="blob-num js-line-number" data-line-number="784"></td>
        <td id="LC784" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>dimName</span>[<span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;DimID&quot;</span>))] <span class=pl-c1>in</span> <span class=pl-s1>dimensionsIncrements</span>:</td>
      </tr>
      <tr>
        <td id="L785" class="blob-num js-line-number" data-line-number="785"></td>
        <td id="LC785" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>raise</span> <span class=pl-v>Exception</span>(<span class=pl-s>&#39;You can<span class=pl-cce>\&#39;</span>t set %s in serie %s&#39;</span> <span class=pl-c1>%</span> (</td>
      </tr>
      <tr>
        <td id="L786" class="blob-num js-line-number" data-line-number="786"></td>
        <td id="LC786" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>dimName</span>[<span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;DimID&quot;</span>))],</td>
      </tr>
      <tr>
        <td id="L787" class="blob-num js-line-number" data-line-number="787"></td>
        <td id="LC787" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-en>getName</span>())</td>
      </tr>
      <tr>
        <td id="L788" class="blob-num js-line-number" data-line-number="788"></td>
        <td id="LC788" class="blob-code blob-code-inner js-file-line">                                )</td>
      </tr>
      <tr>
        <td id="L789" class="blob-num js-line-number" data-line-number="789"></td>
        <td id="LC789" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L790" class="blob-num js-line-number" data-line-number="790"></td>
        <td id="LC790" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-s1>self</span>.<span class=pl-en>getOffset</span>(<span class=pl-c1>**</span><span class=pl-s1>dimensionsIncrements</span>))</td>
      </tr>
      <tr>
        <td id="L791" class="blob-num js-line-number" data-line-number="791"></td>
        <td id="LC791" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>shape</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>get2DShape</span>()</td>
      </tr>
      <tr>
        <td id="L792" class="blob-num js-line-number" data-line-number="792"></td>
        <td id="LC792" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>np</span>.<span class=pl-en>fromfile</span>(</td>
      </tr>
      <tr>
        <td id="L793" class="blob-num js-line-number" data-line-number="793"></td>
        <td id="LC793" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>f</span>,</td>
      </tr>
      <tr>
        <td id="L794" class="blob-num js-line-number" data-line-number="794"></td>
        <td id="LC794" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>dtype</span><span class=pl-c1>=</span><span class=pl-s1>np</span>.<span class=pl-s1>ubyte</span>,</td>
      </tr>
      <tr>
        <td id="L795" class="blob-num js-line-number" data-line-number="795"></td>
        <td id="LC795" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>count</span><span class=pl-c1>=</span><span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerSlice</span>()</td>
      </tr>
      <tr>
        <td id="L796" class="blob-num js-line-number" data-line-number="796"></td>
        <td id="LC796" class="blob-code blob-code-inner js-file-line">        ).<span class=pl-en>reshape</span>(<span class=pl-s1>shape</span>)</td>
      </tr>
      <tr>
        <td id="L797" class="blob-num js-line-number" data-line-number="797"></td>
        <td id="LC797" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L798" class="blob-num js-line-number" data-line-number="798"></td>
        <td id="LC798" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>get2DString</span>(<span class=pl-s1>self</span>, <span class=pl-c1>**</span><span class=pl-s1>dimensionsIncrements</span>):</td>
      </tr>
      <tr>
        <td id="L799" class="blob-num js-line-number" data-line-number="799"></td>
        <td id="LC799" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L800" class="blob-num js-line-number" data-line-number="800"></td>
        <td id="LC800" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Use the two first dimensions as image dimension</span></td>
      </tr>
      <tr>
        <td id="L801" class="blob-num js-line-number" data-line-number="801"></td>
        <td id="LC801" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L802" class="blob-num js-line-number" data-line-number="802"></td>
        <td id="LC802" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-en>getDimensions</span>()[:<span class=pl-c1>2</span>]:</td>
      </tr>
      <tr>
        <td id="L803" class="blob-num js-line-number" data-line-number="803"></td>
        <td id="LC803" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>dimName</span>[<span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;DimID&quot;</span>))] <span class=pl-c1>in</span> <span class=pl-s1>dimensionsIncrements</span>:</td>
      </tr>
      <tr>
        <td id="L804" class="blob-num js-line-number" data-line-number="804"></td>
        <td id="LC804" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>raise</span> <span class=pl-v>Exception</span>(<span class=pl-s>&#39;You can<span class=pl-cce>\&#39;</span>t set %s in serie %s&#39;</span> <span class=pl-c1>%</span> (</td>
      </tr>
      <tr>
        <td id="L805" class="blob-num js-line-number" data-line-number="805"></td>
        <td id="LC805" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>dimName</span>[<span class=pl-en>int</span>(<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&quot;DimID&quot;</span>))],</td>
      </tr>
      <tr>
        <td id="L806" class="blob-num js-line-number" data-line-number="806"></td>
        <td id="LC806" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-en>getName</span>()))</td>
      </tr>
      <tr>
        <td id="L807" class="blob-num js-line-number" data-line-number="807"></td>
        <td id="LC807" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L808" class="blob-num js-line-number" data-line-number="808"></td>
        <td id="LC808" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-s1>self</span>.<span class=pl-en>getOffset</span>(<span class=pl-c1>**</span><span class=pl-s1>dimensionsIncrements</span>))</td>
      </tr>
      <tr>
        <td id="L809" class="blob-num js-line-number" data-line-number="809"></td>
        <td id="LC809" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerSlice</span>())</td>
      </tr>
      <tr>
        <td id="L810" class="blob-num js-line-number" data-line-number="810"></td>
        <td id="LC810" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L811" class="blob-num js-line-number" data-line-number="811"></td>
        <td id="LC811" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L812" class="blob-num js-line-number" data-line-number="812"></td>
        <td id="LC812" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L813" class="blob-num js-line-number" data-line-number="813"></td>
        <td id="LC813" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getFrame</span>(<span class=pl-s1>self</span>, <span class=pl-s1>channel</span><span class=pl-c1>=</span><span class=pl-c1>0</span>, <span class=pl-v>T</span><span class=pl-c1>=</span><span class=pl-c1>0</span>, <span class=pl-s1>dtype</span><span class=pl-c1>=</span><span class=pl-s1>np</span>.<span class=pl-s1>uint8</span>):</td>
      </tr>
      <tr>
        <td id="L814" class="blob-num js-line-number" data-line-number="814"></td>
        <td id="LC814" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L815" class="blob-num js-line-number" data-line-number="815"></td>
        <td id="LC815" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return a numpy array (C order, thus last index is X):</span></td>
      </tr>
      <tr>
        <td id="L816" class="blob-num js-line-number" data-line-number="816"></td>
        <td id="LC816" class="blob-code blob-code-inner js-file-line"><span class=pl-s>         2D if XYT or XZT serie,</span></td>
      </tr>
      <tr>
        <td id="L817" class="blob-num js-line-number" data-line-number="817"></td>
        <td id="LC817" class="blob-code blob-code-inner js-file-line"><span class=pl-s>         3D if XYZ, XYZT or XZYT</span></td>
      </tr>
      <tr>
        <td id="L818" class="blob-num js-line-number" data-line-number="818"></td>
        <td id="LC818" class="blob-code blob-code-inner js-file-line"><span class=pl-s>         (ok if no T dependence)</span></td>
      </tr>
      <tr>
        <td id="L819" class="blob-num js-line-number" data-line-number="819"></td>
        <td id="LC819" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Leica use uint8 by default, but after deconvolution the datatype is np.uint16</span></td>
      </tr>
      <tr>
        <td id="L820" class="blob-num js-line-number" data-line-number="820"></td>
        <td id="LC820" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L821" class="blob-num js-line-number" data-line-number="821"></td>
        <td id="LC821" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>zcyx</span> <span class=pl-c1>=</span> []</td>
      </tr>
      <tr>
        <td id="L822" class="blob-num js-line-number" data-line-number="822"></td>
        <td id="LC822" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>channels</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>getChannels</span>()</td>
      </tr>
      <tr>
        <td id="L823" class="blob-num js-line-number" data-line-number="823"></td>
        <td id="LC823" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>z</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-s1>self</span>.<span class=pl-en>getBoxShape</span>()[<span class=pl-c1>-</span><span class=pl-c1>1</span>]):</td>
      </tr>
      <tr>
        <td id="L824" class="blob-num js-line-number" data-line-number="824"></td>
        <td id="LC824" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>cyx</span> <span class=pl-c1>=</span> []</td>
      </tr>
      <tr>
        <td id="L825" class="blob-num js-line-number" data-line-number="825"></td>
        <td id="LC825" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>i</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-en>len</span>(<span class=pl-s1>channels</span>)):</td>
      </tr>
      <tr>
        <td id="L826" class="blob-num js-line-number" data-line-number="826"></td>
        <td id="LC826" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-s1>self</span>.<span class=pl-en>getOffset</span>(<span class=pl-c1>**</span><span class=pl-en>dict</span>({<span class=pl-s>&#39;T&#39;</span>: <span class=pl-v>T</span>, <span class=pl-s>&#39;Z&#39;</span>: <span class=pl-s1>z</span>})) <span class=pl-c1>+</span> <span class=pl-s1>self</span>.<span class=pl-en>getChannelOffset</span>(<span class=pl-s1>i</span>))</td>
      </tr>
      <tr>
        <td id="L827" class="blob-num js-line-number" data-line-number="827"></td>
        <td id="LC827" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>yx</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>fromfile</span>(<span class=pl-s1>self</span>.<span class=pl-s1>f</span>, <span class=pl-s1>dtype</span><span class=pl-c1>=</span><span class=pl-s1>dtype</span>, <span class=pl-s1>count</span><span class=pl-c1>=</span><span class=pl-en>int</span>(<span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerSlice</span>()))</td>
      </tr>
      <tr>
        <td id="L828" class="blob-num js-line-number" data-line-number="828"></td>
        <td id="LC828" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>yx</span> <span class=pl-c1>=</span> <span class=pl-s1>yx</span>.<span class=pl-en>reshape</span>(<span class=pl-s1>self</span>.<span class=pl-en>get2DShape</span>())</td>
      </tr>
      <tr>
        <td id="L829" class="blob-num js-line-number" data-line-number="829"></td>
        <td id="LC829" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>cyx</span>.<span class=pl-en>append</span>(<span class=pl-s1>yx</span>)</td>
      </tr>
      <tr>
        <td id="L830" class="blob-num js-line-number" data-line-number="830"></td>
        <td id="LC830" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>zcyx</span>.<span class=pl-en>append</span>(<span class=pl-s1>cyx</span>)</td>
      </tr>
      <tr>
        <td id="L831" class="blob-num js-line-number" data-line-number="831"></td>
        <td id="LC831" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>zcyx</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>array</span>(<span class=pl-s1>zcyx</span>)</td>
      </tr>
      <tr>
        <td id="L832" class="blob-num js-line-number" data-line-number="832"></td>
        <td id="LC832" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>xzcy</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>moveaxis</span>(<span class=pl-s1>zcyx</span>, <span class=pl-c1>-</span><span class=pl-c1>1</span>, <span class=pl-c1>0</span>)</td>
      </tr>
      <tr>
        <td id="L833" class="blob-num js-line-number" data-line-number="833"></td>
        <td id="LC833" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>xyzc</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>moveaxis</span>(<span class=pl-s1>xzcy</span>, <span class=pl-c1>-</span><span class=pl-c1>1</span>, <span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L834" class="blob-num js-line-number" data-line-number="834"></td>
        <td id="LC834" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>xyzc</span>[:, :, :, <span class=pl-s1>channel</span>]</td>
      </tr>
      <tr>
        <td id="L835" class="blob-num js-line-number" data-line-number="835"></td>
        <td id="LC835" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L836" class="blob-num js-line-number" data-line-number="836"></td>
        <td id="LC836" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L837" class="blob-num js-line-number" data-line-number="837"></td>
        <td id="LC837" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L838" class="blob-num js-line-number" data-line-number="838"></td>
        <td id="LC838" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L839" class="blob-num js-line-number" data-line-number="839"></td>
        <td id="LC839" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getFrame2D</span>(<span class=pl-s1>self</span>, <span class=pl-s1>channel</span><span class=pl-c1>=</span><span class=pl-c1>0</span>, <span class=pl-v>T</span><span class=pl-c1>=</span><span class=pl-c1>0</span>, <span class=pl-s1>dtype</span><span class=pl-c1>=</span><span class=pl-s1>np</span>.<span class=pl-s1>uint8</span>):</td>
      </tr>
      <tr>
        <td id="L840" class="blob-num js-line-number" data-line-number="840"></td>
        <td id="LC840" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L841" class="blob-num js-line-number" data-line-number="841"></td>
        <td id="LC841" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Method: Get a 2D image from the serie XY (for XY, XYT) or XZ (for XZ, XZT)</span></td>
      </tr>
      <tr>
        <td id="L842" class="blob-num js-line-number" data-line-number="842"></td>
        <td id="LC842" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L843" class="blob-num js-line-number" data-line-number="843"></td>
        <td id="LC843" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        kwarg:: channel number (int, default = 0), Time index (int, default = 0)</span></td>
      </tr>
      <tr>
        <td id="L844" class="blob-num js-line-number" data-line-number="844"></td>
        <td id="LC844" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        </span></td>
      </tr>
      <tr>
        <td id="L845" class="blob-num js-line-number" data-line-number="845"></td>
        <td id="LC845" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Return: a 2D numpy array (in C order: last index is X). (ok if no T dependence)</span></td>
      </tr>
      <tr>
        <td id="L846" class="blob-num js-line-number" data-line-number="846"></td>
        <td id="LC846" class="blob-code blob-code-inner js-file-line"><span class=pl-s>                Leica use uint8 by default, but after deconvolution the datatype is np.uint16</span></td>
      </tr>
      <tr>
        <td id="L847" class="blob-num js-line-number" data-line-number="847"></td>
        <td id="LC847" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L848" class="blob-num js-line-number" data-line-number="848"></td>
        <td id="LC848" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>channels</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>getChannels</span>()</td>
      </tr>
      <tr>
        <td id="L849" class="blob-num js-line-number" data-line-number="849"></td>
        <td id="LC849" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>cyx</span> <span class=pl-c1>=</span> []</td>
      </tr>
      <tr>
        <td id="L850" class="blob-num js-line-number" data-line-number="850"></td>
        <td id="LC850" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>i</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-en>len</span>(<span class=pl-s1>channels</span>)):</td>
      </tr>
      <tr>
        <td id="L851" class="blob-num js-line-number" data-line-number="851"></td>
        <td id="LC851" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-s1>self</span>.<span class=pl-en>getOffset</span>(<span class=pl-c1>**</span><span class=pl-en>dict</span>({<span class=pl-s>&#39;T&#39;</span>: <span class=pl-v>T</span>})) <span class=pl-c1>+</span> <span class=pl-s1>self</span>.<span class=pl-en>getChannelOffset</span>(<span class=pl-s1>i</span>))</td>
      </tr>
      <tr>
        <td id="L852" class="blob-num js-line-number" data-line-number="852"></td>
        <td id="LC852" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>yx</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>fromfile</span>(<span class=pl-s1>self</span>.<span class=pl-s1>f</span>, <span class=pl-s1>dtype</span><span class=pl-c1>=</span><span class=pl-s1>dtype</span>, <span class=pl-s1>count</span><span class=pl-c1>=</span><span class=pl-en>int</span>(<span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerSlice</span>()))</td>
      </tr>
      <tr>
        <td id="L853" class="blob-num js-line-number" data-line-number="853"></td>
        <td id="LC853" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>yx</span> <span class=pl-c1>=</span> <span class=pl-s1>yx</span>.<span class=pl-en>reshape</span>(<span class=pl-s1>self</span>.<span class=pl-en>get2DShape</span>())</td>
      </tr>
      <tr>
        <td id="L854" class="blob-num js-line-number" data-line-number="854"></td>
        <td id="LC854" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>cyx</span>.<span class=pl-en>append</span>(<span class=pl-s1>yx</span>)</td>
      </tr>
      <tr>
        <td id="L855" class="blob-num js-line-number" data-line-number="855"></td>
        <td id="LC855" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>cyx</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>array</span>(<span class=pl-s1>cyx</span>)</td>
      </tr>
      <tr>
        <td id="L856" class="blob-num js-line-number" data-line-number="856"></td>
        <td id="LC856" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>cyx</span>[<span class=pl-s1>channel</span>]</td>
      </tr>
      <tr>
        <td id="L857" class="blob-num js-line-number" data-line-number="857"></td>
        <td id="LC857" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L858" class="blob-num js-line-number" data-line-number="858"></td>
        <td id="LC858" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L859" class="blob-num js-line-number" data-line-number="859"></td>
        <td id="LC859" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L860" class="blob-num js-line-number" data-line-number="860"></td>
        <td id="LC860" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getMetadata</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L861" class="blob-num js-line-number" data-line-number="861"></td>
        <td id="LC861" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L862" class="blob-num js-line-number" data-line-number="862"></td>
        <td id="LC862" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        voxel size unit: µm</span></td>
      </tr>
      <tr>
        <td id="L863" class="blob-num js-line-number" data-line-number="863"></td>
        <td id="LC863" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L864" class="blob-num js-line-number" data-line-number="864"></td>
        <td id="LC864" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nbx</span>, <span class=pl-s1>nby</span>, <span class=pl-s1>nbz</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>getBoxShape</span>()</td>
      </tr>
      <tr>
        <td id="L865" class="blob-num js-line-number" data-line-number="865"></td>
        <td id="LC865" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>setting_records</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&#39;ScannerSettingRecord&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L866" class="blob-num js-line-number" data-line-number="866"></td>
        <td id="LC866" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>dimension_descriptions</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>getElementsByTagName</span>(<span class=pl-s>&#39;DimensionDescription&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L867" class="blob-num js-line-number" data-line-number="867"></td>
        <td id="LC867" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>setting_records</span>:</td>
      </tr>
      <tr>
        <td id="L868" class="blob-num js-line-number" data-line-number="868"></td>
        <td id="LC868" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># ScannerSettingRecord only available for some lif files!</span></td>
      </tr>
      <tr>
        <td id="L869" class="blob-num js-line-number" data-line-number="869"></td>
        <td id="LC869" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>psx</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>getVoxelSize</span>(<span class=pl-c1>1</span>)  <span class=pl-c># m ---&gt; µm</span></td>
      </tr>
      <tr>
        <td id="L870" class="blob-num js-line-number" data-line-number="870"></td>
        <td id="LC870" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>psy</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>getVoxelSize</span>(<span class=pl-c1>2</span>)  <span class=pl-c># m ---&gt; µm</span></td>
      </tr>
      <tr>
        <td id="L871" class="blob-num js-line-number" data-line-number="871"></td>
        <td id="LC871" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>psz</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>getVoxelSize</span>(<span class=pl-c1>3</span>)  <span class=pl-c># m ---&gt; µm</span></td>
      </tr>
      <tr>
        <td id="L872" class="blob-num js-line-number" data-line-number="872"></td>
        <td id="LC872" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>unit_x</span> <span class=pl-c1>=</span> [<span class=pl-s1>s</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Unit&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>s</span> <span class=pl-c1>in</span> <span class=pl-s1>setting_records</span> <span class=pl-k>if</span> <span class=pl-s1>s</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Identifier&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;dblVoxelX&#39;</span>][<span class=pl-c1>0</span>]</td>
      </tr>
      <tr>
        <td id="L873" class="blob-num js-line-number" data-line-number="873"></td>
        <td id="LC873" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>unit_y</span> <span class=pl-c1>=</span> [<span class=pl-s1>s</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Unit&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>s</span> <span class=pl-c1>in</span> <span class=pl-s1>setting_records</span> <span class=pl-k>if</span> <span class=pl-s1>s</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Identifier&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;dblVoxelY&#39;</span>][<span class=pl-c1>0</span>]</td>
      </tr>
      <tr>
        <td id="L874" class="blob-num js-line-number" data-line-number="874"></td>
        <td id="LC874" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>unit_z</span> <span class=pl-c1>=</span> [<span class=pl-s1>s</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Unit&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>s</span> <span class=pl-c1>in</span> <span class=pl-s1>setting_records</span> <span class=pl-k>if</span> <span class=pl-s1>s</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Identifier&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;dblVoxelZ&#39;</span>][<span class=pl-c1>0</span>]</td>
      </tr>
      <tr>
        <td id="L875" class="blob-num js-line-number" data-line-number="875"></td>
        <td id="LC875" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>units</span> <span class=pl-c1>=</span> [<span class=pl-s1>unit_x</span>, <span class=pl-s1>unit_y</span>, <span class=pl-s1>unit_z</span>]</td>
      </tr>
      <tr>
        <td id="L876" class="blob-num js-line-number" data-line-number="876"></td>
        <td id="LC876" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>dimension_descriptions</span>:</td>
      </tr>
      <tr>
        <td id="L877" class="blob-num js-line-number" data-line-number="877"></td>
        <td id="LC877" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># Use DimensionDescription to get voxel information</span></td>
      </tr>
      <tr>
        <td id="L878" class="blob-num js-line-number" data-line-number="878"></td>
        <td id="LC878" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>length_x</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L879" class="blob-num js-line-number" data-line-number="879"></td>
        <td id="LC879" class="blob-code blob-code-inner js-file-line">                [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Length&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span> <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;1&#39;</span>][<span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L880" class="blob-num js-line-number" data-line-number="880"></td>
        <td id="LC880" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>length_y</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L881" class="blob-num js-line-number" data-line-number="881"></td>
        <td id="LC881" class="blob-code blob-code-inner js-file-line">                [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Length&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span> <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;2&#39;</span>][<span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L882" class="blob-num js-line-number" data-line-number="882"></td>
        <td id="LC882" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>length_z</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L883" class="blob-num js-line-number" data-line-number="883"></td>
        <td id="LC883" class="blob-code blob-code-inner js-file-line">                [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Length&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span> <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;3&#39;</span>][<span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L884" class="blob-num js-line-number" data-line-number="884"></td>
        <td id="LC884" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>number_x</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L885" class="blob-num js-line-number" data-line-number="885"></td>
        <td id="LC885" class="blob-code blob-code-inner js-file-line">                [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;NumberOfElements&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span> <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;1&#39;</span>][</td>
      </tr>
      <tr>
        <td id="L886" class="blob-num js-line-number" data-line-number="886"></td>
        <td id="LC886" class="blob-code blob-code-inner js-file-line">                    <span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L887" class="blob-num js-line-number" data-line-number="887"></td>
        <td id="LC887" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>number_y</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L888" class="blob-num js-line-number" data-line-number="888"></td>
        <td id="LC888" class="blob-code blob-code-inner js-file-line">                [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;NumberOfElements&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span> <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;2&#39;</span>][</td>
      </tr>
      <tr>
        <td id="L889" class="blob-num js-line-number" data-line-number="889"></td>
        <td id="LC889" class="blob-code blob-code-inner js-file-line">                    <span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L890" class="blob-num js-line-number" data-line-number="890"></td>
        <td id="LC890" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>number_z</span> <span class=pl-c1>=</span> <span class=pl-en>float</span>(</td>
      </tr>
      <tr>
        <td id="L891" class="blob-num js-line-number" data-line-number="891"></td>
        <td id="LC891" class="blob-code blob-code-inner js-file-line">                [<span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;NumberOfElements&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>d</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span> <span class=pl-k>if</span> <span class=pl-s1>d</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;DimID&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;3&#39;</span>][</td>
      </tr>
      <tr>
        <td id="L892" class="blob-num js-line-number" data-line-number="892"></td>
        <td id="LC892" class="blob-code blob-code-inner js-file-line">                    <span class=pl-c1>0</span>])</td>
      </tr>
      <tr>
        <td id="L893" class="blob-num js-line-number" data-line-number="893"></td>
        <td id="LC893" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>psx</span> <span class=pl-c1>=</span> <span class=pl-s1>length_x</span> <span class=pl-c1>/</span> <span class=pl-s1>number_x</span></td>
      </tr>
      <tr>
        <td id="L894" class="blob-num js-line-number" data-line-number="894"></td>
        <td id="LC894" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>psy</span> <span class=pl-c1>=</span> <span class=pl-s1>length_y</span> <span class=pl-c1>/</span> <span class=pl-s1>number_y</span></td>
      </tr>
      <tr>
        <td id="L895" class="blob-num js-line-number" data-line-number="895"></td>
        <td id="LC895" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>psz</span> <span class=pl-c1>=</span> <span class=pl-s1>length_z</span> <span class=pl-c1>/</span> <span class=pl-s1>number_z</span></td>
      </tr>
      <tr>
        <td id="L896" class="blob-num js-line-number" data-line-number="896"></td>
        <td id="LC896" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>units</span> <span class=pl-c1>=</span> [<span class=pl-s1>s</span>.<span class=pl-en>getAttribute</span>(<span class=pl-s>&#39;Unit&#39;</span>) <span class=pl-k>for</span> <span class=pl-s1>s</span> <span class=pl-c1>in</span> <span class=pl-s1>dimension_descriptions</span>]</td>
      </tr>
      <tr>
        <td id="L897" class="blob-num js-line-number" data-line-number="897"></td>
        <td id="LC897" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L898" class="blob-num js-line-number" data-line-number="898"></td>
        <td id="LC898" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>RuntimeError</span>(<span class=pl-s>&quot;Can&#39;t find voxel information in the lif file!&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L899" class="blob-num js-line-number" data-line-number="899"></td>
        <td id="LC899" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L900" class="blob-num js-line-number" data-line-number="900"></td>
        <td id="LC900" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-en>len</span>(<span class=pl-en>set</span>(<span class=pl-s1>units</span>)) <span class=pl-c1>==</span> <span class=pl-c1>1</span> <span class=pl-c1>and</span> <span class=pl-s>&#39;m&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>units</span>:</td>
      </tr>
      <tr>
        <td id="L901" class="blob-num js-line-number" data-line-number="901"></td>
        <td id="LC901" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>factor</span> <span class=pl-c1>=</span> <span class=pl-c1>1e6</span></td>
      </tr>
      <tr>
        <td id="L902" class="blob-num js-line-number" data-line-number="902"></td>
        <td id="LC902" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>unit</span> <span class=pl-c1>=</span> <span class=pl-s>&#39;um&#39;</span></td>
      </tr>
      <tr>
        <td id="L903" class="blob-num js-line-number" data-line-number="903"></td>
        <td id="LC903" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L904" class="blob-num js-line-number" data-line-number="904"></td>
        <td id="LC904" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>warnings</span>.<span class=pl-en>warn</span>(<span class=pl-s>&#39;unit is not meter, check the unit of voxel size&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L905" class="blob-num js-line-number" data-line-number="905"></td>
        <td id="LC905" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>factor</span> <span class=pl-c1>=</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L906" class="blob-num js-line-number" data-line-number="906"></td>
        <td id="LC906" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>unit</span> <span class=pl-c1>=</span> <span class=pl-s>&quot;, &quot;</span>.<span class=pl-en>join</span>(<span class=pl-s1>units</span>)</td>
      </tr>
      <tr>
        <td id="L907" class="blob-num js-line-number" data-line-number="907"></td>
        <td id="LC907" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L908" class="blob-num js-line-number" data-line-number="908"></td>
        <td id="LC908" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>psx</span> <span class=pl-c1>=</span> <span class=pl-s1>psx</span> <span class=pl-c1>*</span> <span class=pl-s1>factor</span>  <span class=pl-c># m ---&gt; µm</span></td>
      </tr>
      <tr>
        <td id="L909" class="blob-num js-line-number" data-line-number="909"></td>
        <td id="LC909" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>psy</span> <span class=pl-c1>=</span> <span class=pl-s1>psy</span> <span class=pl-c1>*</span> <span class=pl-s1>factor</span>  <span class=pl-c># m ---&gt; µm</span></td>
      </tr>
      <tr>
        <td id="L910" class="blob-num js-line-number" data-line-number="910"></td>
        <td id="LC910" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>psz</span> <span class=pl-c1>=</span> <span class=pl-s1>psz</span> <span class=pl-c1>*</span> <span class=pl-s1>factor</span>  <span class=pl-c># m ---&gt; µm</span></td>
      </tr>
      <tr>
        <td id="L911" class="blob-num js-line-number" data-line-number="911"></td>
        <td id="LC911" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L912" class="blob-num js-line-number" data-line-number="912"></td>
        <td id="LC912" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> {</td>
      </tr>
      <tr>
        <td id="L913" class="blob-num js-line-number" data-line-number="913"></td>
        <td id="LC913" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&#39;voxel_size_x&#39;</span>: <span class=pl-s1>psx</span>,</td>
      </tr>
      <tr>
        <td id="L914" class="blob-num js-line-number" data-line-number="914"></td>
        <td id="LC914" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&#39;voxel_size_y&#39;</span>: <span class=pl-s1>psy</span>,</td>
      </tr>
      <tr>
        <td id="L915" class="blob-num js-line-number" data-line-number="915"></td>
        <td id="LC915" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&#39;voxel_size_z&#39;</span>: <span class=pl-s1>psz</span>,</td>
      </tr>
      <tr>
        <td id="L916" class="blob-num js-line-number" data-line-number="916"></td>
        <td id="LC916" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&#39;voxel_size_unit&#39;</span>: <span class=pl-s1>unit</span>,</td>
      </tr>
      <tr>
        <td id="L917" class="blob-num js-line-number" data-line-number="917"></td>
        <td id="LC917" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&#39;voxel_number_x&#39;</span>: <span class=pl-s1>nbx</span>,</td>
      </tr>
      <tr>
        <td id="L918" class="blob-num js-line-number" data-line-number="918"></td>
        <td id="LC918" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&#39;voxel_number_y&#39;</span>: <span class=pl-s1>nby</span>,</td>
      </tr>
      <tr>
        <td id="L919" class="blob-num js-line-number" data-line-number="919"></td>
        <td id="LC919" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&#39;voxel_number_z&#39;</span>: <span class=pl-s1>nbz</span>,</td>
      </tr>
      <tr>
        <td id="L920" class="blob-num js-line-number" data-line-number="920"></td>
        <td id="LC920" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&#39;channel_number&#39;</span>: <span class=pl-en>len</span>(<span class=pl-s1>self</span>.<span class=pl-en>getChannels</span>()),</td>
      </tr>
      <tr>
        <td id="L921" class="blob-num js-line-number" data-line-number="921"></td>
        <td id="LC921" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&#39;frame_number&#39;</span>: <span class=pl-s1>self</span>.<span class=pl-en>getNbFrames</span>(),</td>
      </tr>
      <tr>
        <td id="L922" class="blob-num js-line-number" data-line-number="922"></td>
        <td id="LC922" class="blob-code blob-code-inner js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L923" class="blob-num js-line-number" data-line-number="923"></td>
        <td id="LC923" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L924" class="blob-num js-line-number" data-line-number="924"></td>
        <td id="LC924" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>saveXML</span>(<span class=pl-s1>self</span>, <span class=pl-s1>name</span><span class=pl-c1>=</span><span class=pl-c1>None</span>):</td>
      </tr>
      <tr>
        <td id="L925" class="blob-num js-line-number" data-line-number="925"></td>
        <td id="LC925" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>name</span>:</td>
      </tr>
      <tr>
        <td id="L926" class="blob-num js-line-number" data-line-number="926"></td>
        <td id="LC926" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>name</span> <span class=pl-c1>=</span> <span class=pl-s>&#39;{}.xml&#39;</span>.<span class=pl-en>format</span>(<span class=pl-s1>self</span>.<span class=pl-en>getName</span>())</td>
      </tr>
      <tr>
        <td id="L927" class="blob-num js-line-number" data-line-number="927"></td>
        <td id="LC927" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>with</span> <span class=pl-en>open</span>(<span class=pl-s1>name</span>, <span class=pl-s>&#39;w&#39;</span>) <span class=pl-k>as</span> <span class=pl-s1>f</span>:</td>
      </tr>
      <tr>
        <td id="L928" class="blob-num js-line-number" data-line-number="928"></td>
        <td id="LC928" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>f</span>.<span class=pl-en>write</span>(<span class=pl-s1>self</span>.<span class=pl-s1>root</span>.<span class=pl-en>toprettyxml</span>())</td>
      </tr>
      <tr>
        <td id="L929" class="blob-num js-line-number" data-line-number="929"></td>
        <td id="LC929" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L930" class="blob-num js-line-number" data-line-number="930"></td>
        <td id="LC930" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>getVTK</span>(<span class=pl-s1>self</span>, <span class=pl-s1>fname</span>, <span class=pl-v>T</span><span class=pl-c1>=</span><span class=pl-c1>0</span>):</td>
      </tr>
      <tr>
        <td id="L931" class="blob-num js-line-number" data-line-number="931"></td>
        <td id="LC931" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L932" class="blob-num js-line-number" data-line-number="932"></td>
        <td id="LC932" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Export the frame at time T to a vtk file</span></td>
      </tr>
      <tr>
        <td id="L933" class="blob-num js-line-number" data-line-number="933"></td>
        <td id="LC933" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        One can render the vtk file using software like Paraview</span></td>
      </tr>
      <tr>
        <td id="L934" class="blob-num js-line-number" data-line-number="934"></td>
        <td id="LC934" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L935" class="blob-num js-line-number" data-line-number="935"></td>
        <td id="LC935" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;.vtk&#39;</span> <span class=pl-c1>not</span> <span class=pl-c1>in</span> <span class=pl-s1>fname</span>:</td>
      </tr>
      <tr>
        <td id="L936" class="blob-num js-line-number" data-line-number="936"></td>
        <td id="LC936" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>fname</span> <span class=pl-c1>+=</span> <span class=pl-s>&#39;.vtk&#39;</span></td>
      </tr>
      <tr>
        <td id="L937" class="blob-num js-line-number" data-line-number="937"></td>
        <td id="LC937" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>with</span> <span class=pl-en>open</span>(<span class=pl-s1>fname</span>, <span class=pl-s>&#39;wb&#39;</span>) <span class=pl-k>as</span> <span class=pl-s1>f</span>:</td>
      </tr>
      <tr>
        <td id="L938" class="blob-num js-line-number" data-line-number="938"></td>
        <td id="LC938" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>header</span> <span class=pl-c1>=</span> <span class=pl-s>&#39;# vtk DataFile Version 3.0<span class=pl-cce>\n</span>%s<span class=pl-cce>\n</span>&#39;</span> <span class=pl-c1>%</span> <span class=pl-s1>self</span>.<span class=pl-s1>getName</span> <span class=pl-c1>+</span>\</td>
      </tr>
      <tr>
        <td id="L939" class="blob-num js-line-number" data-line-number="939"></td>
        <td id="LC939" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&#39;BINARY<span class=pl-cce>\n</span>DATASET STRUCTURED_POINTS<span class=pl-cce>\n</span>&#39;</span> <span class=pl-c1>+</span>\</td>
      </tr>
      <tr>
        <td id="L940" class="blob-num js-line-number" data-line-number="940"></td>
        <td id="LC940" class="blob-code blob-code-inner js-file-line">                (<span class=pl-s>&#39;DIMENSIONS %d %d %d<span class=pl-cce>\n</span>&#39;</span> <span class=pl-c1>%</span> <span class=pl-en>tuple</span>(<span class=pl-s1>self</span>.<span class=pl-en>getBoxShape</span>())) <span class=pl-c1>+</span>\</td>
      </tr>
      <tr>
        <td id="L941" class="blob-num js-line-number" data-line-number="941"></td>
        <td id="LC941" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&#39;ORIGIN 0 0 0<span class=pl-cce>\n</span>&#39;</span> <span class=pl-c1>+</span>\</td>
      </tr>
      <tr>
        <td id="L942" class="blob-num js-line-number" data-line-number="942"></td>
        <td id="LC942" class="blob-code blob-code-inner js-file-line">                (<span class=pl-s>&#39;SPACING 1 1 %g<span class=pl-cce>\n</span>&#39;</span> <span class=pl-c1>%</span> <span class=pl-s1>self</span>.<span class=pl-en>getZXratio</span>()) <span class=pl-c1>+</span>\</td>
      </tr>
      <tr>
        <td id="L943" class="blob-num js-line-number" data-line-number="943"></td>
        <td id="LC943" class="blob-code blob-code-inner js-file-line">                (<span class=pl-s>&#39;POINT_DATA %d<span class=pl-cce>\n</span>&#39;</span> <span class=pl-c1>%</span> <span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerFrame</span>()) <span class=pl-c1>+</span>\</td>
      </tr>
      <tr>
        <td id="L944" class="blob-num js-line-number" data-line-number="944"></td>
        <td id="LC944" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&#39;SCALARS Intensity unsigned_char<span class=pl-cce>\n</span>LOOKUP_TABLE default<span class=pl-cce>\n</span>&#39;</span></td>
      </tr>
      <tr>
        <td id="L945" class="blob-num js-line-number" data-line-number="945"></td>
        <td id="LC945" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>f</span>.<span class=pl-en>write</span>(<span class=pl-s1>str</span>.<span class=pl-en>encode</span>(<span class=pl-s1>header</span>))</td>
      </tr>
      <tr>
        <td id="L946" class="blob-num js-line-number" data-line-number="946"></td>
        <td id="LC946" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-s1>self</span>.<span class=pl-en>getOffset</span>(<span class=pl-c1>**</span><span class=pl-en>dict</span>({<span class=pl-s>&#39;T&#39;</span>: <span class=pl-v>T</span>})))</td>
      </tr>
      <tr>
        <td id="L947" class="blob-num js-line-number" data-line-number="947"></td>
        <td id="LC947" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>f</span>.<span class=pl-en>write</span>(<span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>read</span>(<span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerFrame</span>()))</td>
      </tr>
      <tr>
        <td id="L948" class="blob-num js-line-number" data-line-number="948"></td>
        <td id="LC948" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L949" class="blob-num js-line-number" data-line-number="949"></td>
        <td id="LC949" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>enumByFrame</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L950" class="blob-num js-line-number" data-line-number="950"></td>
        <td id="LC950" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;yield time steps one after the other as a couple (time,numpy array). It is not safe to combine this syntax with getFrame or get2DSlice.&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L951" class="blob-num js-line-number" data-line-number="951"></td>
        <td id="LC951" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>yield</span> <span class=pl-c1>0</span>, <span class=pl-s1>self</span>.<span class=pl-en>getFrame</span>()</td>
      </tr>
      <tr>
        <td id="L952" class="blob-num js-line-number" data-line-number="952"></td>
        <td id="LC952" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>t</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-c1>1</span>, <span class=pl-s1>self</span>.<span class=pl-en>getNbFrames</span>()):</td>
      </tr>
      <tr>
        <td id="L953" class="blob-num js-line-number" data-line-number="953"></td>
        <td id="LC953" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>yield</span> <span class=pl-s1>t</span>, <span class=pl-s1>np</span>.<span class=pl-en>fromfile</span>(</td>
      </tr>
      <tr>
        <td id="L954" class="blob-num js-line-number" data-line-number="954"></td>
        <td id="LC954" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>f</span>,</td>
      </tr>
      <tr>
        <td id="L955" class="blob-num js-line-number" data-line-number="955"></td>
        <td id="LC955" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>dtype</span><span class=pl-c1>=</span><span class=pl-s1>np</span>.<span class=pl-s1>ubyte</span>,</td>
      </tr>
      <tr>
        <td id="L956" class="blob-num js-line-number" data-line-number="956"></td>
        <td id="LC956" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>count</span><span class=pl-c1>=</span><span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerFrame</span>()</td>
      </tr>
      <tr>
        <td id="L957" class="blob-num js-line-number" data-line-number="957"></td>
        <td id="LC957" class="blob-code blob-code-inner js-file-line">            ).<span class=pl-en>reshape</span>(<span class=pl-s1>self</span>.<span class=pl-en>getFrameShape</span>())</td>
      </tr>
      <tr>
        <td id="L958" class="blob-num js-line-number" data-line-number="958"></td>
        <td id="LC958" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L959" class="blob-num js-line-number" data-line-number="959"></td>
        <td id="LC959" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>enumBySlice</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L960" class="blob-num js-line-number" data-line-number="960"></td>
        <td id="LC960" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;yield 2D slices one after the other as a 3-tuple (time,z,numpy array). It is not safe to combine this syntax with getFrame or get2DSlice.&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L961" class="blob-num js-line-number" data-line-number="961"></td>
        <td id="LC961" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>f</span>.<span class=pl-en>seek</span>(<span class=pl-s1>self</span>.<span class=pl-en>getOffset</span>())</td>
      </tr>
      <tr>
        <td id="L962" class="blob-num js-line-number" data-line-number="962"></td>
        <td id="LC962" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>t</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-s1>self</span>.<span class=pl-en>getNbFrames</span>()):</td>
      </tr>
      <tr>
        <td id="L963" class="blob-num js-line-number" data-line-number="963"></td>
        <td id="LC963" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>z</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerFrame</span>() <span class=pl-c1>/</span> <span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerSlice</span>()):</td>
      </tr>
      <tr>
        <td id="L964" class="blob-num js-line-number" data-line-number="964"></td>
        <td id="LC964" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>yield</span> <span class=pl-s1>t</span>, <span class=pl-s1>z</span>, <span class=pl-s1>np</span>.<span class=pl-en>fromfile</span>(</td>
      </tr>
      <tr>
        <td id="L965" class="blob-num js-line-number" data-line-number="965"></td>
        <td id="LC965" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-s1>f</span>,</td>
      </tr>
      <tr>
        <td id="L966" class="blob-num js-line-number" data-line-number="966"></td>
        <td id="LC966" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>dtype</span><span class=pl-c1>=</span><span class=pl-s1>np</span>.<span class=pl-s1>ubyte</span>,</td>
      </tr>
      <tr>
        <td id="L967" class="blob-num js-line-number" data-line-number="967"></td>
        <td id="LC967" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>count</span><span class=pl-c1>=</span><span class=pl-s1>self</span>.<span class=pl-en>getNbPixelsPerSlice</span>()</td>
      </tr>
      <tr>
        <td id="L968" class="blob-num js-line-number" data-line-number="968"></td>
        <td id="LC968" class="blob-code blob-code-inner js-file-line">                ).<span class=pl-en>reshape</span>(<span class=pl-s1>self</span>.<span class=pl-en>get2DShape</span>())</td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 9C8.82843 9 9.5 8.32843 9.5 7.5C9.5 6.67157 8.82843 6 8 6C7.17157 6 6.5 6.67157 6.5 7.5C6.5 8.32843 7.17157 9 8 9Z"></path>
  <path d="M1.5 9C2.32843 9 3 8.32843 3 7.5C3 6.67157 2.32843 6 1.5 6C0.671573 6 0 6.67157 0 7.5C0 8.32843 0.671573 9 1.5 9Z"></path>
  <path d="M14.5 9C15.3284 9 16 8.32843 16 7.5C16 6.67157 15.3284 6 14.5 6C13.6716 6 13 6.67157 13 7.5C13 8.32843 13.6716 9 14.5 9Z"></path></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;">
            Copy lines
          </clipboard-copy>
        </li>
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;">
            Copy permalink
          </clipboard-copy>
        </li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/raulbenitez/MITO_FIBERS/blame/5007d0e818614a4bd334cee8d1c41c4e5a01b0b2/read_lif.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/raulbenitez/MITO_FIBERS/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get">
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover"
     hidden
     data-tagsearch-url="/raulbenitez/MITO_FIBERS/find-symbols"
     data-tagsearch-ref="master"
     data-tagsearch-path="read_lif.py"
     data-tagsearch-lang="Python"
     data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:265504996,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/raulbenitez/MITO_FIBERS/blob/master/read_lif.py&quot;,&quot;user_id&quot;:34841791}}"
     data-hydro-click-hmac="bd21c5bf9b5f7a084529642385609a5a8921b878aae3004f5689830531c01304">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box box-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>



  </div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2020 GitHub, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>

    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8C0 11.54 2.29 14.53 5.47 15.59C5.87 15.66 6.02 15.42 6.02 15.21C6.02 15.02 6.01 14.39 6.01 13.72C4 14.09 3.48 13.23 3.32 12.78C3.23 12.55 2.84 11.84 2.5 11.65C2.22 11.5 1.82 11.13 2.49 11.12C3.12 11.11 3.57 11.7 3.72 11.94C4.44 13.15 5.59 12.81 6.05 12.6C6.12 12.08 6.33 11.73 6.56 11.53C4.78 11.33 2.92 10.64 2.92 7.58C2.92 6.71 3.23 5.99 3.74 5.43C3.66 5.23 3.38 4.41 3.82 3.31C3.82 3.31 4.49 3.1 6.02 4.13C6.66 3.95 7.34 3.86 8.02 3.86C8.7 3.86 9.38 3.95 10.02 4.13C11.55 3.09 12.22 3.31 12.22 3.31C12.66 4.41 12.38 5.23 12.3 5.43C12.81 5.99 13.12 6.7 13.12 7.58C13.12 10.65 11.25 11.33 9.47 11.53C9.76 11.78 10.01 12.26 10.01 13.01C10.01 14.08 10 14.94 10 15.21C10 15.42 10.15 15.67 10.55 15.59C13.71 14.53 16 11.53 16 8C16 3.58 12.42 0 8 0Z"></path></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.22048 1.75358C8.1263 1.57738 7.87369 1.57738 7.77951 1.75359L1.69787 13.1321C1.60886 13.2987 1.72953 13.5 1.91835 13.5H14.0816C14.2705 13.5 14.3911 13.2987 14.3021 13.1321L8.22048 1.75358ZM6.45662 1.04652C7.11588 -0.186933 8.88412 -0.186935 9.54338 1.04652L15.625 12.4251C16.2481 13.5908 15.4034 15 14.0816 15H1.91835C0.596554 15 -0.248093 13.5908 0.374974 12.4251L6.45662 1.04652ZM9 11C9 11.5523 8.55229 12 8 12C7.44772 12 7 11.5523 7 11C7 10.4477 7.44772 10 8 10C8.55229 10 9 10.4477 9 11ZM8.75 5.75C8.75 5.33579 8.41421 5 8 5C7.58579 5 7.25 5.33579 7.25 5.75V8.25C7.25 8.66421 7.58579 9 8 9C8.41421 9 8.75 8.66421 8.75 8.25V5.75Z"></path></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.72 3.72C3.86062 3.57955 4.05125 3.50066 4.25 3.50066C4.44875 3.50066 4.63937 3.57955 4.78 3.72L8 6.94L11.22 3.72C11.2887 3.64631 11.3715 3.58721 11.4635 3.54622C11.5555 3.50523 11.6548 3.48319 11.7555 3.48141C11.8562 3.47963 11.9562 3.49816 12.0496 3.53588C12.143 3.5736 12.2278 3.62974 12.299 3.70096C12.3703 3.77218 12.4264 3.85702 12.4641 3.9504C12.5018 4.04379 12.5204 4.14382 12.5186 4.24452C12.5168 4.34523 12.4948 4.44454 12.4538 4.53654C12.4128 4.62854 12.3537 4.71134 12.28 4.78L9.06 8L12.28 11.22C12.3537 11.2887 12.4128 11.3715 12.4538 11.4635C12.4948 11.5555 12.5168 11.6548 12.5186 11.7555C12.5204 11.8562 12.5018 11.9562 12.4641 12.0496C12.4264 12.143 12.3703 12.2278 12.299 12.299C12.2278 12.3703 12.143 12.4264 12.0496 12.4641C11.9562 12.5018 11.8562 12.5204 11.7555 12.5186C11.6548 12.5168 11.5555 12.4948 11.4635 12.4538C11.3715 12.4128 11.2887 12.3537 11.22 12.28L8 9.06L4.78 12.28C4.63782 12.4125 4.44977 12.4846 4.25547 12.4812C4.06117 12.4777 3.87579 12.399 3.73837 12.2616C3.60096 12.1242 3.52225 11.9388 3.51882 11.7445C3.51539 11.5502 3.58752 11.3622 3.72 11.22L6.94 8L3.72 4.78C3.57955 4.63938 3.50066 4.44875 3.50066 4.25C3.50066 4.05125 3.57955 3.86063 3.72 3.72Z"></path></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" async="async" integrity="sha512-WcQmT2vhcClFVOaaAJV/M+HqsJ2Gq/myvl6F3gCVBxykazXTs+i5fvxncSXwyG1CSfcrqmLFw/R/bmFYzprX2A==" type="application/javascript" id="js-conditional-compat" data-src="https://github.githubassets.com/assets/compat-bootstrap-59c4264f.js"></script>
    <script crossorigin="anonymous" integrity="sha512-Y86V8OBlvF6I/7e56GKOOt80Yg1RTGA09uqFFX18aiBtevLbKGxB7sVpCn79fukppFIBqyBTB/s6l0Bhn0kidQ==" type="application/javascript" src="https://github.githubassets.com/assets/environment-bootstrap-63ce95f0.js"></script>
    <script crossorigin="anonymous" async="async" integrity="sha512-ASMgX6+DJ9LVZX/3Fj0RzibSpfigU83ubvsxxwriojWmuBM3faUp1108gypkhXpqLHEBQhIhjlzDOejzOFd0gA==" type="application/javascript" src="https://github.githubassets.com/assets/vendor-0123205f.js"></script>
    <script crossorigin="anonymous" async="async" integrity="sha512-/m8I1HkTKfQgD4Lqec5vpR0qqCNHDINqdqbHHZnQDDaJff7C2KUPTSbPwu0Xhv2br1ccJkb3OtrrWyPWmbHPHw==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-fe6f08d4.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-7zUqOlU/OYZXIucAoxZq68H226nzDYpOeio8mhcUnVDkjOyG0bvHAPTpiUcYXaCxYZEndg5SJ72j7d0Tx+EtOw==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-ef352a3a.js"></script>
    
        <script crossorigin="anonymous" async="async" integrity="sha512-4GcSWGoe36+BoWho4gtJcByZe8j43w+lt2/PDe3rmBxRVSgD29YipDwuIywe8fvOd2b2CszBqaPGxSznUtE3Xg==" type="application/javascript" data-module-id="./drag-drop.js" data-src="https://github.githubassets.com/assets/drag-drop-e0671258.js"></script>
        <script crossorigin="anonymous" async="async" integrity="sha512-3Vk1NFIOm+TBUMM6pTA6DCUwwLLnc/QIT8jpENm71InvSU8O4p2plDagpst1tH1l+9jOBnneaXZnAskA9a2b3w==" type="application/javascript" data-module-id="./gist-vendor.js" data-src="https://github.githubassets.com/assets/gist-vendor-dd593534.js"></script>
        <script crossorigin="anonymous" async="async" integrity="sha512-urN6bhHnHu4C12A+cTH3dOp+CwLaycy2HUXr95hvu5pbYRdF8z6iR+UQcTZutQ6mZG3Njluw2MTZVCNmwcqh8g==" type="application/javascript" data-module-id="./randomColor.js" data-src="https://github.githubassets.com/assets/randomColor-bab37a6e.js"></script>
    
    
  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.22048 1.75358C8.1263 1.57738 7.87369 1.57738 7.77951 1.75359L1.69787 13.1321C1.60886 13.2987 1.72953 13.5 1.91835 13.5H14.0816C14.2705 13.5 14.3911 13.2987 14.3021 13.1321L8.22048 1.75358ZM6.45662 1.04652C7.11588 -0.186933 8.88412 -0.186935 9.54338 1.04652L15.625 12.4251C16.2481 13.5908 15.4034 15 14.0816 15H1.91835C0.596554 15 -0.248093 13.5908 0.374974 12.4251L6.45662 1.04652ZM9 11C9 11.5523 8.55229 12 8 12C7.44772 12 7 11.5523 7 11C7 10.4477 7.44772 10 8 10C8.55229 10 9 10.4477 9 11ZM8.75 5.75C8.75 5.33579 8.41421 5 8 5C7.58579 5 7.25 5.33579 7.25 5.75V8.25C7.25 8.66421 7.58579 9 8 9C8.41421 9 8.75 8.66421 8.75 8.25V5.75Z"></path></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" clip-rule="evenodd" d="M3.72 3.72C3.86062 3.57955 4.05125 3.50066 4.25 3.50066C4.44875 3.50066 4.63937 3.57955 4.78 3.72L8 6.94L11.22 3.72C11.2887 3.64631 11.3715 3.58721 11.4635 3.54622C11.5555 3.50523 11.6548 3.48319 11.7555 3.48141C11.8562 3.47963 11.9562 3.49816 12.0496 3.53588C12.143 3.5736 12.2278 3.62974 12.299 3.70096C12.3703 3.77218 12.4264 3.85702 12.4641 3.9504C12.5018 4.04379 12.5204 4.14382 12.5186 4.24452C12.5168 4.34523 12.4948 4.44454 12.4538 4.53654C12.4128 4.62854 12.3537 4.71134 12.28 4.78L9.06 8L12.28 11.22C12.3537 11.2887 12.4128 11.3715 12.4538 11.4635C12.4948 11.5555 12.5168 11.6548 12.5186 11.7555C12.5204 11.8562 12.5018 11.9562 12.4641 12.0496C12.4264 12.143 12.3703 12.2278 12.299 12.299C12.2278 12.3703 12.143 12.4264 12.0496 12.4641C11.9562 12.5018 11.8562 12.5204 11.7555 12.5186C11.6548 12.5168 11.5555 12.4948 11.4635 12.4538C11.3715 12.4128 11.2887 12.3537 11.22 12.28L8 9.06L4.78 12.28C4.63782 12.4125 4.44977 12.4846 4.25547 12.4812C4.06117 12.4777 3.87579 12.399 3.73837 12.2616C3.60096 12.1242 3.52225 11.9388 3.51882 11.7445C3.51539 11.5502 3.58752 11.3622 3.72 11.22L6.94 8L3.72 4.78C3.57955 4.63938 3.50066 4.44875 3.50066 4.25C3.50066 4.05125 3.57955 3.86063 3.72 3.72Z"></path></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>


  </body>
</html>

