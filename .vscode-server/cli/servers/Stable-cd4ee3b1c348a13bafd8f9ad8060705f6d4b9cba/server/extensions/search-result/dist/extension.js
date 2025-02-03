(()=>{"use strict";var e={256:function(e,t,n){var i,r=this&&this.__createBinding||(Object.create?function(e,t,n,i){void 0===i&&(i=n);var r=Object.getOwnPropertyDescriptor(t,n);r&&!("get"in r?!t.__esModule:r.writable||r.configurable)||(r={enumerable:!0,get:function(){return t[n]}}),Object.defineProperty(e,i,r)}:function(e,t,n,i){void 0===i&&(i=n),e[i]=t[n]}),o=this&&this.__setModuleDefault||(Object.create?function(e,t){Object.defineProperty(e,"default",{enumerable:!0,value:t})}:function(e,t){e.default=t}),a=this&&this.__importStar||(i=function(e){return i=Object.getOwnPropertyNames||function(e){var t=[];for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&(t[t.length]=n);return t},i(e)},function(e){if(e&&e.__esModule)return e;var t={};if(null!=e)for(var n=i(e),a=0;a<n.length;a++)"default"!==n[a]&&r(t,e,n[a]);return o(t,e),t});Object.defineProperty(t,"__esModule",{value:!0}),t.activate=function(e){const t=s.window.createTextEditorDecorationType({opacity:"0.7"}),n=s.window.createTextEditorDecorationType({fontWeight:"bold"}),i=e=>{const i=R(e.document).filter(m),r=i.filter((e=>e.isContext)).map((e=>e.prefixRange)),o=i.filter((e=>!e.isContext)).map((e=>e.prefixRange));e.setDecorations(t,r),e.setDecorations(n,o)};s.window.activeTextEditor&&"search-result"===s.window.activeTextEditor.document.languageId&&i(s.window.activeTextEditor),e.subscriptions.push(s.languages.registerDocumentSymbolProvider(d,{provideDocumentSymbols:(e,t)=>R(e,t).filter(w).map((e=>new s.DocumentSymbol(e.path,"",s.SymbolKind.File,e.allLocations.map((({originSelectionRange:e})=>e)).reduce(((e,t)=>e.union(t)),e.location.originSelectionRange),e.location.originSelectionRange)))}),s.languages.registerCompletionItemProvider(d,{provideCompletionItems(e,t){const n=e.lineAt(t.line);if(t.line>3)return[];if(0===t.character||1===t.character&&"#"===n.text){const n=Array.from({length:f.length}).map(((t,n)=>e.lineAt(n).text));return f.filter((e=>n.every((t=>-1===t.indexOf(e))))).map((e=>({label:e,insertText:e.slice(t.character)+" "})))}return-1===n.text.indexOf("# Flags:")?[]:p.filter((e=>-1===n.text.indexOf(e))).map((e=>({label:e,insertText:e+" "})))}},"#"),s.languages.registerDefinitionProvider(d,{provideDefinition(e,t,n){const i=R(e,n)[t.line];if(!i)return[];if("file"===i.type)return i.allLocations.map((e=>({...e,originSelectionRange:i.location.originSelectionRange})));const r=i.locations.find((e=>e.originSelectionRange.contains(t)));if(!r)return[];const o=new s.Position(r.targetSelectionRange.start.line,r.targetSelectionRange.start.character+(t.character-r.originSelectionRange.start.character));return[{...r,targetSelectionRange:new s.Range(o,o)}]}}),s.languages.registerDocumentLinkProvider(d,{provideDocumentLinks:async(e,t)=>R(e,t).filter(w).map((({location:e})=>({range:e.originSelectionRange,target:e.targetUri})))}),s.window.onDidChangeActiveTextEditor((e=>{"search-result"===e?.document.languageId&&(h=void 0,x?.dispose(),x=s.workspace.onDidChangeTextDocument((t=>{t.document.uri===e.document.uri&&i(e)})),i(e))})),{dispose(){h=void 0,x?.dispose()}})};const s=a(n(398)),c=a(n(928)),l=/^(\S.*):$/,g=/^(\s+)(\d+)(: |  )(\s*)(.*)$/,u=/⟪ ([0-9]+) characters skipped ⟫/g,d={language:"search-result",exclusive:!0},f=["# Query:","# Flags:","# Including:","# Excluding:","# ContextLines:"],p=["RegExp","CaseSensitive","IgnoreExcludeSettings","WordMatch"];let h,x;function v(e,t){if(e.startsWith("(Settings) "))return s.Uri.file(e.slice(11)).with({scheme:"vscode-userdata"});if(c.isAbsolute(e))return/^[\\\/]Untitled-\d*$/.test(e)?s.Uri.file(e.slice(1)).with({scheme:"untitled",path:e.slice(1)}):s.Uri.file(e);if(0===e.indexOf("~/")){const t=process.env.HOME||process.env.HOMEPATH||"";return s.Uri.file(c.join(t,e.slice(2)))}const n=(e,t)=>s.Uri.joinPath(e.uri,t);if(s.workspace.workspaceFolders){const i=/^(.*) • (.*)$/.exec(e);if(i){const[,e,t]=i,r=s.workspace.workspaceFolders.filter((t=>t.name===e))[0];if(r)return n(r,t)}else{if(1===s.workspace.workspaceFolders.length)return n(s.workspace.workspaceFolders[0],e);if("untitled"!==t.scheme){const i=s.workspace.workspaceFolders.filter((e=>t.toString().startsWith(e.uri.toString())))[0];if(i)return n(i,e)}}}console.error(`Unable to resolve path ${e}`)}const w=e=>"file"===e.type,m=e=>"result"===e.type;function R(e,t){if(h&&h.uri===e.uri&&h.version===e.version)return h.parse;const n=e.getText().split(/\r?\n/),i=[];let r,o;for(let a=0;a<n.length;a++){if(t?.isCancellationRequested)return[];const c=n[a],d=l.exec(c);if(d){const[,t]=d;if(r=v(t,e.uri),!r)continue;o=[];const n={targetRange:new s.Range(0,0,0,1),targetUri:r,originSelectionRange:new s.Range(a,0,a,c.length)};i[a]={type:"file",location:n,allLocations:o,path:t}}if(!r)continue;const f=g.exec(c);if(f){const[,e,t,n]=f,l=+t-1,g=(e+t+n).length,d=new s.Range(Math.max(l-3,0),0,l+3,c.length),p=[];let h=g,x=0;u.lastIndex=g;for(let e;e=u.exec(c);)p.push({targetRange:d,targetSelectionRange:new s.Range(l,x,l,x),targetUri:r,originSelectionRange:new s.Range(a,h,a,u.lastIndex-e[0].length)}),x+=u.lastIndex-h-e[0].length+Number(e[1]),h=u.lastIndex;h<c.length&&p.push({targetRange:d,targetSelectionRange:new s.Range(l,x,l,x),targetUri:r,originSelectionRange:new s.Range(a,h,a,c.length)}),n.includes(":")&&o?.push(...p);const v={targetRange:d,targetSelectionRange:new s.Range(l,0,l,1),targetUri:r,originSelectionRange:new s.Range(a,0,a,g-1)};p.push(v),i[a]={type:"result",locations:p,isContext:" "===n,prefixRange:new s.Range(a,0,a,g)}}}return h={version:e.version,parse:i,uri:e.uri},i}},398:e=>{e.exports=require("vscode")},928:e=>{e.exports=require("path")}},t={},n=function n(i){var r=t[i];if(void 0!==r)return r.exports;var o=t[i]={exports:{}};return e[i].call(o.exports,o,o.exports,n),o.exports}(256),i=exports;for(var r in n)i[r]=n[r];n.__esModule&&Object.defineProperty(i,"__esModule",{value:!0})})();
//# sourceMappingURL=https://main.vscode-cdn.net/sourcemaps/cd4ee3b1c348a13bafd8f9ad8060705f6d4b9cba/extensions/search-result/dist/extension.js.map