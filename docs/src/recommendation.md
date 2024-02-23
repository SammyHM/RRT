# Recomendation

<table>
  <tr>
    <td>
      <div style="font-weight: bold;">@property <br> MAX_PUBS</div>
      <div style="font-style: italic;">Defines the maximun number of publications to be requested at once.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">@property <br> SLEEP_TIMER</div>
      <div style="font-style: italic;">Defines the number of seconds between each publication request.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def next_publication(publications: iter) &rarr; Publication:</div>
      <div style="font-style: italic;">Given a publication iterable, sleeps the application for some time and returns the next publication.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def search_pubs(query: str) &rarr; list():</div>
      <div style="font-style: italic;">Given a topic, returns a list of Publication type objects.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def best_publication(pubs: list()) &rarr; Publication:</div>
      <div style="font-style: italic;">Given a list of Publication type objects, returns the publication with the best score.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def fetch_pdf_data(publication: Publication) &rarr; None:</div>
      <div style="font-style: italic;">Given a publication, fetches the pdf from its associated url.</div>
    </td>
  </tr>
  <tr>
    <td>
      <div style="font-weight: bold;">def parse_pdf_data(publication: Publication) &rarr; str:</div>
      <div style="font-style: italic;">Given a publication, parses data that has been stored at data/pdf/{name} and returns its text formated.</div>
    </td>
  </tr>
</table>
