erfan4lx = (function(){
    
    MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

    var SCROLL_INTERVAL = 600, 
        SCROLL_INCREMENT = 450, 
        AUTO_SCROLL = true,
        NAME_PREFIX = '',
        UNKNOWN_CONTACTS_ONLY = false, 
        MEMBERS_QUEUE = {},
        TOTAL_MEMBERS;

    var scrollInterval, observer, membersList, header;


    var start = function(){

        membersList = document.querySelectorAll('span[title=You]')[0]?.parentNode?.parentNode?.parentNode?.parentNode?.parentNode?.parentNode?.parentNode;
        header = document.getElementsByTagName('header')[0];

        if(!membersList){
            document.querySelector("#main > header").firstChild.click();
            membersList = document.querySelectorAll('span[title=You]')[0]?.parentNode?.parentNode?.parentNode?.parentNode?.parentNode?.parentNode?.parentNode;
            header = document.getElementsByTagName('header')[0];
        }

        observer = new MutationObserver(function (mutations, observer) {   
            scrapeData(); // fired when a mutation occurs
        });
    

        observer.observe(membersList, {
            childList: true,
            subtree: true
        });

        TOTAL_MEMBERS = membersList.parentElement.parentElement.querySelector('span').innerText.match(/\d+/)[0]*1;
        
        document.querySelector("span[data-icon=down]")?.click()


        header.nextSibling.scrollTop = 100;
        scrapeData();

        if(AUTO_SCROLL) scrollInterval = setInterval(autoScroll, SCROLL_INTERVAL);    
    }


})();

erfan4lx.quickExport()
